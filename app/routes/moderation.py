from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.post("/moderate/{id}")
async def moderation():
    pass
