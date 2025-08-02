from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.utils.token import get_current_user
import os

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)

IMAGE_DIR = "static/images"

@router.get(
        "/images/{id}",
        summary="Получить готовое изображение",
        description="Гет запрос на получение изображения по айди"
)
async def get_id_image(id: str):
    file_path = os.path.join(IMAGE_DIR, f"{id}.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(file_path, media_type="image/png")

@router.post(
        "/images/{id}/rate",
        summary="Оценить картинку для метрики",
        description="Поставить оценку полученной картики для улучшения качества"
)
async def rate_image():
    pass

