from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.history_model import HistoryRequest, HistoryResponse
from app.database import get_db
from app.models.client import Client
from app.models.history import History
from passlib.context import CryptContext
from typing import List
from app.utils.token import get_current_user

router = APIRouter()
pwd_context  = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post(
        "/history/",
        summary="Получить историю запросов",
        description="Вся история запросов доступна по этому ендпоинту",
        response_model=List[HistoryResponse]
)
async def get_history(
    data: HistoryRequest, 
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    result = await db.execute(select(Client).where(Client.email == data.email))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    result = await db.execute(select(History).where(History.user_id == user.id))
    history_records = result.scalars().all()

    return history_records
