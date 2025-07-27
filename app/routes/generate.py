from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import BaseModel
from app.utils.token import get_current_user
from app.services.image_generator import generate_image
from uuid import uuid4

router = APIRouter()

@router.post("/generate/")
async def generate(prompt_data: dict, background_tasks: BackgroundTasks):
    prompt = prompt_data.get("prompt")
    num_images = int(prompt_data.get("num_images", 1))
    num_images = min(max(num_images, 1), 10)

    results = []

    for _ in range(num_images):
        image_id = uuid4().hex
        background_tasks.add_task(generate_image, prompt, image_id)

        results.append({
            "id": image_id,
            "title": prompt,
            "image_url": f"images/{image_id}"
        })
    
    return results
