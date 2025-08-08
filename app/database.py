from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .core.config import get_settings
from app.models.base import Base

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
