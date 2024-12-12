from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import UUID as PGUUID, VARCHAR as PGVARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import uuid4

from api.database.db import Base


class User(Base):
    """Модель пользователя."""

    __tablename__ = "users"

    uid = Column(PGUUID, primary_key=True, default=uuid4)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(PGVARCHAR, nullable=False, server_default="user")
    is_verified = Column(Boolean, default=False)
    password_hash = Column(PGVARCHAR, nullable=False)
    created_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now())

    hotels = relationship("Hotel", back_populates="user")
    reviews = relationship("Review", back_populates="user")

    def __repr__(self):
        return f"<User  {self.username}>"