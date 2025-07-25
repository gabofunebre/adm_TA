import os
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql+psycopg2://postgres:postgres@db:5432/movdb')
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY', 'changeme')
    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = '.env'

@lru_cache()
def get_settings():
    return Settings()
