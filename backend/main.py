# main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import router as api_router
from database import Base, engine, get_db
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

# Create all database t
# bind=engine)
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://yourdomain.com",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows only specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

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
