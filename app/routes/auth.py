from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from app.schemas import user

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {}

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/auth/register")
async def register(user: user.UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    fake_users_db[user.email] = {
        "email": user.email,
        "hashed_password": hashed_password,
        "is_active": False
    }
    
    return {"msg": "User created successfully", "result": fake_users_db}

@router.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"msg": f"Welcome {form_data.username}"}
