from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, Field

AllowedStatus = Literal["applied", "interviewing", "offer", "rejected", "withdrawn"]


class ApplicationBase(BaseModel):
    company_name: str = Field(..., min_length=1, max_length=120)
    job_title: str = Field(..., min_length=1, max_length=120)
    application_date: date
    status: AllowedStatus = "applied"
    interview_round: int = Field(0, ge=0, le=10)
    notes: str | None = Field(default=None, max_length=2000)
    result: str | None = Field(default="pending", max_length=100)


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    company_name: str | None = Field(default=None, min_length=1, max_length=120)
    job_title: str | None = Field(default=None, min_length=1, max_length=120)
    application_date: date | None = None
    status: AllowedStatus | None = None
    interview_round: int | None = Field(default=None, ge=0, le=10)
    notes: str | None = Field(default=None, max_length=2000)
    result: str | None = Field(default=None, max_length=100)


class ApplicationResponse(ApplicationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ApplicationSummaryResponse(BaseModel):
    total_applications: int
    status_breakdown: dict[str, int]
    result_breakdown: dict[str, int]
    average_interview_round: float
