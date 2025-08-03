from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
import enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from app.database import Base
import enum

class ActionType(enum.Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"

class AdminAction(Base):
    __tablename__ = "AdminAction"

    id = Column(UUID(as_uuid=True), primary_key=True , default=uuid4)
    admin_id = Column(UUID(as_uuid=True), ForeignKey("Client.id"))
    target_image_id = Column(UUID(as_uuid=True), ForeignKey("Image.id"))
    action_type = Column(Enum(ActionType))
    reason = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
