from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from core.config import settings

user_name = settings.DB_USER_NAME
password = settings.DB_PASSWORD
host = settings.DB_HOST
port = settings.DB_PORT
database_name = settings.DB_DATABASE_NAME

DATABASE_URI = f"mysql://{user_name}:{password}@{host}:{port}/{database_name}?charset=utf-8"

engine = create_engine(
    DATABASE_URI,
    encoding="utf-8"
)

SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
