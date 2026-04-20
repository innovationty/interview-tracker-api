from collections import Counter

from sqlalchemy import or_
from sqlalchemy.orm import Session

from . import models, schemas


def create_application(db: Session, application_data: schemas.ApplicationCreate) -> models.Application:
    """Create and return a new application record."""
    db_application = models.Application(**application_data.model_dump())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


def get_all_applications(
    db: Session,
    page: int = 1,
    page_size: int = 20,
) -> list[models.Application]:
    """Return applications with simple pagination, newest first."""
    offset_value = (page - 1) * page_size
    return (
        db.query(models.Application)
        .order_by(models.Application.id.desc())
        .offset(offset_value)
        .limit(page_size)
        .all()
    )


def get_application_by_id(db: Session, application_id: int) -> models.Application | None:
    """Return one application by ID, or None if not found."""
    return db.query(models.Application).filter(models.Application.id == application_id).first()


def update_application(
    db: Session,
    application_id: int,
    update_data: schemas.ApplicationUpdate,
) -> models.Application | None:
    """Update an existing application and return it, or None if not found."""
    db_application = get_application_by_id(db, application_id)
    if db_application is None:
        return None

    changes = update_data.model_dump(exclude_unset=True)
    for field_name, value in changes.items():
        setattr(db_application, field_name, value)

    db.commit()
    db.refresh(db_application)
    return db_application


def delete_application(db: Session, application_id: int) -> bool:
    """Delete an application by ID. Return True if deleted, False if not found."""
    db_application = get_application_by_id(db, application_id)
    if db_application is None:
        return False

    db.delete(db_application)
    db.commit()
    return True


def filter_applications_by_status(db: Session, status: str) -> list[models.Application]:
    """Return applications that match a status."""
    return (
        db.query(models.Application)
        .filter(models.Application.status == status)
        .order_by(models.Application.id.desc())
        .all()
    )


def search_applications(db: Session, keyword: str) -> list[models.Application]:
    """Search applications by company name or job title."""
    pattern = f"%{keyword}%"
    return (
        db.query(models.Application)
        .filter(
            or_(
                models.Application.company_name.ilike(pattern),
                models.Application.job_title.ilike(pattern),
            )
        )
        .order_by(models.Application.id.desc())
        .all()
    )


def get_application_summary(db: Session) -> schemas.ApplicationSummaryResponse:
    """Return simple summary metrics for dashboard/report use."""
    rows = db.query(models.Application).all()
    total_count = len(rows)

    status_breakdown = Counter(item.status for item in rows)
    result_breakdown = Counter((item.result or "pending") for item in rows)

    if total_count == 0:
        avg_round = 0.0
    else:
        avg_round = round(sum(item.interview_round for item in rows) / total_count, 2)

    return schemas.ApplicationSummaryResponse(
        total_applications=total_count,
        status_breakdown=dict(status_breakdown),
        result_breakdown=dict(result_breakdown),
        average_interview_round=avg_round,
    )
