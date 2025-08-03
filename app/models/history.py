from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from uuid import uuid4
from datetime import datetime

class History(Base):
    __tablename__ = "History"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("Client.id"), nullable=False)
    prompt_text = Column(String, nullable=False)
    num_images = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    
