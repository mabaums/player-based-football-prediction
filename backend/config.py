# config.py

from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    """
    Configuration settings for the application.

    Attributes:
        DATABASE_URL (str): The URL for the PostgreSQL database.
    """
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
