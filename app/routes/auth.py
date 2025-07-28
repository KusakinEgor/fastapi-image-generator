from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from app.schemas import user_model
from app.utils.token import create_access_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {}

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return {"sub": username}

@router.post("/auth/register")
async def register(user: user_model.UserCreate):
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
    user = authenticate_user(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": f"{user}"})
    return {"access_token": access_token, "token_type": "bearer"}
