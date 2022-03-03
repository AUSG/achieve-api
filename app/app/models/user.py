from sqlalchemy import Column, String

from db.base import Base


class User(Base):
    id = Column(String, primary_key=True, index=True)
    display_name = Column(String)

    class Config:
        orm_mode = True
