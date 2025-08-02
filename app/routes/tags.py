from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get(
        "/tags/",
        summary="Теги",
        description="Получить изображения по данному тегу"
)
async def free_tags():
    pass
