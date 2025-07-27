from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/history/")
async def get_history():
    pass
