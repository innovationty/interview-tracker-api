from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite:///./test_job_tracker.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_function():
    # Rebuild test tables before each test so test outcomes are predictable.
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def create_sample_application(
    company_name: str = "TechNova",
    job_title: str = "Backend Developer",
    status: str = "applied",
    interview_round: int = 1,
    result: str = "pending",
):
    """Helper to insert one sample application and return response JSON."""
    response = client.post(
        "/applications",
        json={
            "company_name": company_name,
            "job_title": job_title,
            "application_date": "2026-04-10",
            "status": status,
            "interview_round": interview_round,
            "notes": "Coursework sample note",
            "result": result,
        },
    )
    assert response.status_code == 201
    return response.json()


def test_create_application_record():
    created = create_sample_application()
    assert created["id"] > 0
    assert created["company_name"] == "TechNova"
    assert created["status"] == "applied"


def test_list_all_application_records():
    create_sample_application(company_name="A Corp")
    create_sample_application(company_name="B Corp", status="interviewing")

    response = client.get("/applications")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_list_applications_with_pagination():
    create_sample_application(company_name="Company 1")
    create_sample_application(company_name="Company 2")
    create_sample_application(company_name="Company 3")

    # Request only two records on page 1.
    response = client.get("/applications?page=1&page_size=2")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

    # Request the next page and expect the remaining one record.
    response_page_2 = client.get("/applications?page=2&page_size=2")
    assert response_page_2.status_code == 200
    data_page_2 = response_page_2.json()
    assert len(data_page_2) == 1


def test_get_single_application_record():
    created = create_sample_application(job_title="Junior Backend Developer")
    app_id = created["id"]

    response = client.get(f"/applications/{app_id}")
    assert response.status_code == 200
    assert response.json()["job_title"] == "Junior Backend Developer"


def test_update_application_record():
    created = create_sample_application(status="interviewing", interview_round=2)
    app_id = created["id"]

    updated = client.put(
        f"/applications/{app_id}",
        json={"status": "offer", "interview_round": 3, "result": "Offer received"},
    )
    assert updated.status_code == 200
    assert updated.json()["status"] == "offer"
    assert updated.json()["interview_round"] == 3


def test_delete_application_record():
    created = create_sample_application()
    app_id = created["id"]

    deleted = client.delete(f"/applications/{app_id}")
    assert deleted.status_code == 204


def test_filter_by_status():
    create_sample_application(company_name="DataWorks", status="applied")
    create_sample_application(company_name="CloudEdge", status="interviewing")

    filtered = client.get("/applications/filter?status=interviewing")
    assert filtered.status_code == 200
    data = filtered.json()
    assert len(data) == 1
    assert data[0]["company_name"] == "CloudEdge"


def test_search_by_company_name_or_job_title():
    create_sample_application(company_name="CloudEdge", job_title="Backend Engineer")
    create_sample_application(company_name="OtherCo", job_title="Data Analyst")

    searched = client.get("/applications/search?keyword=cloud")
    assert searched.status_code == 200
    assert len(searched.json()) == 1
    assert searched.json()[0]["company_name"] == "CloudEdge"


def test_summary_endpoint():
    create_sample_application(company_name="DataWorks", status="applied", interview_round=0)
    create_sample_application(company_name="CloudEdge", status="interviewing", interview_round=2)
    create_sample_application(
        company_name="CloudEdge",
        status="offer",
        interview_round=3,
        result="Offer accepted",
    )

    summary = client.get("/applications/summary")
    assert summary.status_code == 200
    summary_data = summary.json()
    assert summary_data["total_applications"] == 3
    assert summary_data["status_breakdown"]["offer"] == 1
    assert summary_data["average_interview_round"] == 1.67


def test_missing_application_record_returns_404():
    response = client.get("/applications/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Application not found"
