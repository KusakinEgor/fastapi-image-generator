from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from app.database import Base

class AuthToken(Base):
    __tablename__ = "AuthToken"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("Client.id"))
    token = Column(String, nullable=False)
    expires_at = Column(DateTime, default=datetime.utcnow)
