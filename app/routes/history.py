from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get(
        "/history/",
        summary="Получить историю запросов",
        description="Вся история запросов доступна по этому ендпоинту"
)
async def get_history():
    pass
