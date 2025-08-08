from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Extra

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    ADMIN_EMAIL: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    MAILER_TOKEN: str
    MAILER_URL: str
    MAILER_FROM: str = 'no-reply@gabo.ar'
    BASE_URL: str

    JWT_ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = '.env'
        extra = Extra.ignore  # Ignora variables como DB_PATH que no se usan acá
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()

