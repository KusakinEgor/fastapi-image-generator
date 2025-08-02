from pydantic import BaseModel, EmailStr, Field

class HistoryPrompt(BaseModel):
    email: EmailStr = Field(..., examples="user@example.com")
    password: str = Field(..., examples="password123")
