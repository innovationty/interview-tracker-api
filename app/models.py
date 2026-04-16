from sqlalchemy import Column, Date, DateTime, Integer, String, Text, func

from .database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(120), nullable=False, index=True)
    job_title = Column(String(120), nullable=False, index=True)
    application_date = Column(Date, nullable=False)
    status = Column(String(30), nullable=False, default="applied", index=True)
    interview_round = Column(Integer, nullable=False, default=0)
    notes = Column(Text, nullable=True)
    result = Column(String(100), nullable=True, default="pending")

    # Automatically set timestamps for record creation and updates.
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
