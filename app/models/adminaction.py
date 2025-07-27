from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from app.database import Base

class AdminAction(Base):
    __tablename__ = "AdminAction"

    id = Column(UUID(as_uuid=True), primary_key=True , default=uuid4)
    admin_id = Column(UUID(as_uuid=True), ForeignKey("poka xz"))
    target_image_id = Column(UUID(as_uuid=True), ForeignKey("Image.id"))
    action_type = Column(Enum)
    reason = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
