from sqlalchemy import String, ForeignKey, DateTime, Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from app.database import Base

class Image(Base):
    __tablename__ = "Image"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    prompt_id = Column(UUID(as_uuid=True), ForeignKey("PromptRequest.id"))
    url = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    format = Column(String, nullable=False)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class ImageTag(Base):
    __tablename__  = "ImageTag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_id = Column(UUID(as_uuid=True), ForeignKey("poka xz"))
    tag_id = Column(UUID(as_uuid=True), ForeignKey("poka xz"))
