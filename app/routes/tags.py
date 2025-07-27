from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/tags/")
async def free_tags():
    pass
