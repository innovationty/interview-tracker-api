from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database file in the project root.
DATABASE_URL = "sqlite:///./job_tracker.db"

# SQLAlchemy engine.
# check_same_thread=False is required for SQLite with FastAPI request handling.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Session factory used by each API request.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for all ORM models.
Base = declarative_base()


def get_db():
    """Provide a database session and close it after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
