from fastapi import APIRouter
from app.schemas.history_model import HistoryPrompt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get(
        "/history/",
        summary="Получить историю запросов",
        description="Вся история запросов доступна по этому ендпоинту"
)
async def get_history(data: HistoryPrompt):
    pass
