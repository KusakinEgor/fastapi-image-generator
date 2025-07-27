from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

router = APIRouter()

IMAGE_DIR = "static/images"

@router.get("/images/{id}")
async def get_id_image(id: str):
    file_path = os.path.join(IMAGE_DIR, f"{id}.png")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(file_path, media_type="image/png")

@router.post("/images/{id}/rate")
async def rate_image():
    pass

