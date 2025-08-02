from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext
from app.schemas.user_model import UserCreate
from app.database import get_db
from app.models.client import Client
from app.models.authtoken import AuthToken
from app.utils.token import create_access_token
from uuid import uuid4
from datetime import datetime

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post(
        "/auth/register",
        summary="Регистрация",
        description="Отправить данные на регистрацию"
)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Client).where(Client.email == user.email))
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    
    db_user = Client(
        id=uuid4(),
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
        is_active=True,
        registered_at=datetime.utcnow(),
        oauth_provider=user.oauth_provider
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return {"msg": "User created successfully", "user_id": db_user.id}

@router.post(
        "/auth/login",
        summary="Логин",
        description="Вход в аккаунт"
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Client).where(Client.email == form_data.username))
    user = result.scalars().first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})

    auth_token = AuthToken(
        id=uuid4(),
        user_id=user.id,
        token=access_token,
        expires_at=datetime.utcnow()
    )

    db.add(auth_token)
    await db.commit()
    await db.refresh(auth_token)

    return {"access_token": access_token, "token_type": "bearer"}
