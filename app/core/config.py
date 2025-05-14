# app/core/config.py
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str = "Amoura AI Service"
    API_V1_STR: str = "/api/v1"

    # Example: API key for a third-party AI service
    OPENAI_API_KEY: Optional[str] = None

    # Add the model_path_sentiment field if you need it
    # model_path_sentiment: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()