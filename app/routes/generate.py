from fastapi import APIRouter, Depends, BackgroundTasks, Request
from app.schemas.generate_model import PromptRequest as Prompt
from app.models.promptrequest import PromptRequest, StatusRequest
from app.utils.token import get_current_user
from app.services.image_generator import generate_image
from app.models.history import History
from uuid import uuid4
from app.models.image import Image
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.rate_limiter import limiter
from datetime import datetime

router = APIRouter()
@router.post(
        "/generate/",
        summary="Сделать генерацию картинки",
        description="Возвращает результат в формате ссылки ⚠️ Ограничение: не более 5 запросов в минуту."
)
@limiter.limit("5/minute")
async def generate(
    prompt_data: Prompt,
    background_tasks: BackgroundTasks,
    request: Request,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
) -> list[dict]:
    prompt = prompt_data.prompt
    num_images = int(prompt_data.num_images or 1)
    num_images = min(max(num_images, 1), 10)

    prompt_entry = PromptRequest(
        id=uuid4(),
        user_id=user.id,
        prompt_text=prompt_data.prompt,
        style="default",
        color_pallette="default",
        quantity=num_images,
        width=512,
        height=512,
        status=StatusRequest.PENDING,
        created_at=datetime.utcnow()
    )

    history_entry = History(
        id=uuid4(),
        user_id=user.id,
        prompt_text=prompt_data.prompt,
        num_images=num_images,
        created_at=datetime.utcnow()
    )

    db.add(history_entry)
    db.add(prompt_entry)
    await db.flush()

    results = []

    for _ in range(num_images):
        image_id = uuid4().hex
        background_tasks.add_task(generate_image, prompt, image_id)

        db_image = Image(
            id=uuid4(),
            prompt_id=prompt_entry.id,
            url=image_id,
            filename=prompt_data.prompt,
            format="Jpg",
            width=12,
            height=12,
            created_at=datetime.utcnow()
        )

        db.add(db_image)
        await db.flush()

        results.append({
            "id": image_id,
            "title": prompt,
            "image_url": f"images/{image_id}"
        })
     
    await db.commit()
    return results
