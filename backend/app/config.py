# backend/app/config.py
import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # General application settings
    DEBUG: bool = Field(default=False, env="DEBUG")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    # Database settings
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    
    # OpenAI API settings
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    OPENAI_API_BASE: str = Field(default="https://api.openai.com/v1", env="OPENAI_API_BASE")
    
    class Config:
        env_file = ".env"              # Load variables from .env file
        env_file_encoding = 'utf-8'

settings = Settings()
