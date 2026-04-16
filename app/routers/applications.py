from fastapi import APIRouter, Depends, HTTPException, Query, Response, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/applications", tags=["Job Applications"])


@router.post(
    "",
    response_model=schemas.ApplicationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create application",
    description="Create a new job application record.",
)
def create_application(
    payload: schemas.ApplicationCreate,
    db: Session = Depends(get_db),
):
    return crud.create_application(db, payload)


@router.get(
    "",
    response_model=list[schemas.ApplicationResponse],
    status_code=status.HTTP_200_OK,
    summary="List all applications",
    description="Return all application records.",
)
def get_all_applications(
    db: Session = Depends(get_db),
):
    return crud.get_all_applications(db)


@router.get(
    "/filter",
    response_model=list[schemas.ApplicationResponse],
    status_code=status.HTTP_200_OK,
    summary="Filter applications by status",
    description="Return applications that match a status value.",
)
def filter_applications_by_status(
    status_value: schemas.AllowedStatus = Query(..., alias="status"),
    db: Session = Depends(get_db),
):
    return crud.filter_applications_by_status(db, status_value)


@router.get(
    "/search",
    response_model=list[schemas.ApplicationResponse],
    status_code=status.HTTP_200_OK,
    summary="Search applications",
    description="Search by company name or job title using a keyword.",
)
def search_applications(
    keyword: str = Query(..., min_length=1, description="Search text for company or job title"),
    db: Session = Depends(get_db),
):
    cleaned = keyword.strip()
    if not cleaned:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Search keyword must not be empty.",
        )
    return crud.search_applications(db, cleaned)


@router.get(
    "/summary",
    response_model=schemas.ApplicationSummaryResponse,
    status_code=status.HTTP_200_OK,
    summary="Get application summary",
    description="Return simple statistics for application progress.",
)
def get_application_summary(db: Session = Depends(get_db)):
    return crud.get_application_summary(db)


@router.get(
    "/{application_id}",
    response_model=schemas.ApplicationResponse,
    status_code=status.HTTP_200_OK,
    summary="Get application by ID",
    description="Return one application record by its ID.",
)
def get_application_by_id(application_id: int, db: Session = Depends(get_db)):
    application = crud.get_application_by_id(db, application_id)
    if application is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    return application


@router.put(
    "/{application_id}",
    response_model=schemas.ApplicationResponse,
    status_code=status.HTTP_200_OK,
    summary="Update application",
    description="Update an existing application record.",
)
def update_application(
    application_id: int,
    payload: schemas.ApplicationUpdate,
    db: Session = Depends(get_db),
):
    application = crud.update_application(db, application_id, payload)
    if application is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    return application


@router.delete(
    "/{application_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete application",
    description="Delete an application record by ID.",
)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_application(db, application_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
