from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Extra

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_port: int
    admin_username: str
    admin_password: str
    google_client_id: str
    google_client_secret: str

    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = '.env'
        extra = Extra.ignore  # Ignora variables como DB_PATH que no se usan acá

@lru_cache()
def get_settings():
    return Settings()

