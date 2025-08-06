from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime

class HistoryRequest(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., example="password123")

class HistoryResponse(BaseModel):
    id: UUID
    prompt_text: str
    num_images: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
