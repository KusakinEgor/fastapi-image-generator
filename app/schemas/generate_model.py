from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    prompt: str = Field(..., example="A cat in space")
    num_images: int = Field(1, ge=1, le=10, example=3)
