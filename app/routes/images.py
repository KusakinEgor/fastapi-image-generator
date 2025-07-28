from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import FileResponse
from app.utils.token import get_current_user
import os

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)

IMAGE_DIR = "static/images"

@router.get("/images/{id}")
async def get_id_image(id: str):
    file_path = os.path.join(IMAGE_DIR, f"{id}.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(file_path, media_type="image/png")

@router.post("/images/{id}/rate")
async def rate_image(id: str):
    pass

