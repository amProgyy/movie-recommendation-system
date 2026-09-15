from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from src.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique= True, nullable=False, index=True)
    password_hash = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))