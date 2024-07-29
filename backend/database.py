# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# Database URL
DATABASE_URL = settings.DATABASE_URL

# Create database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Provides a database session and ensures its closure after use.

    Yields:
        SessionLocal: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
