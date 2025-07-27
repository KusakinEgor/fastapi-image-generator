from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.database import Base

class Rating(Base):
    __tablename__ = "Rating"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("Client.id"))
    image_id = Column(UUID(as_uuid=True), ForeignKey("Image.id"))
    score = Column(Integer)
