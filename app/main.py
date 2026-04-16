from fastapi import FastAPI

from . import models
from .database import Base, engine
from .routers import applications

# Create database tables on startup for coursework simplicity.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Application and Interview Preparation Tracker API",
    description="A simple coursework API for tracking job applications and interview preparation progress.",
    version="1.0.0",
)

app.include_router(applications.router)


@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}
