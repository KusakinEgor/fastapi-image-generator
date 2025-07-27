from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from app.database import Base

class PromptRequest(Base):
    __tablename__ = "PromptRequest"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("Client.id"))
    prompt_text = Column(Text, nullable=False)
    style = Column(String, nullable=False)
    color_pallette = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False, default=100)
    height = Column(Integer, nullable=False, default=100)
    status = Column(Enum)
    note = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

