from typing import TYPE_CHECKING

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Message(Base):
    id = Column(String, primary_key=True, index=True)
    author_id = Column(String, ForeignKey("user.id"))
    author = relationship("User", back_populates="messages")
    content = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    class Config:
        orm_mode = True
