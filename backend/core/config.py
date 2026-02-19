from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    ALOW_ORIGINS: List[str] = []
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        
settings = Settings()