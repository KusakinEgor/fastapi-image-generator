from sqlalchemy import Column, String, Boolean, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from app.database import Base
import enum

class RoleClient(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class Client(Base):
    __tablename__ = "Client"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleClient), nullable=False)
    is_active = Column(Boolean, nullable=False)
    registered_at = Column(DateTime, default=datetime.utcnow)
    oauth_provider = Column(String, nullable=False)

