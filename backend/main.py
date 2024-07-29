# main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import router as api_router
from database import Base, engine, get_db
from pathlib import Path

# Create all database t
# bind=engine)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include API router
app.include_router(api_router)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for FastAPI application. Loads initial data on startup.
    """
    db = next(get_db())
    yield

# Set the lifespan event handler
app.router.lifespan_context = lifespan
