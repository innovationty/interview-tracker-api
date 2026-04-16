# Job Application and Interview Preparation Tracker API

## Project Overview

This project is a backend-only REST API built for university coursework. It helps users track job applications, interview stages, notes, and outcomes in a simple and structured way.

The API is designed to be:

- easy to understand for students
- suitable for Swagger UI demonstration
- suitable for a technical report and oral presentation

## Coursework Purpose

This system demonstrates core web service concepts required in a typical university module:

- API design with clear endpoints
- SQL database integration
- data validation and serialization
- CRUD operations
- structured testing with pytest

## Main Features

- Create a job application record
- List all application records
- Retrieve one application by ID
- Update an existing application
- Delete an application
- Filter records by status
- Search records by company name or job title
- View summary metrics for application progress

## Technology Stack

- FastAPI: web framework and automatic API documentation
- SQLite: lightweight relational database for local development
- SQLAlchemy ORM: model and database interaction layer
- Pydantic: request validation and response schemas
- Uvicorn: ASGI server for running FastAPI
- pytest + TestClient: automated endpoint tests

## Why FastAPI

FastAPI was chosen because it is well suited for coursework projects:

- clear, modern Python syntax
- built-in request validation with Pydantic
- automatic Swagger UI generation
- easy mapping between models, schemas, and endpoints

This makes the project straightforward to explain in an oral exam.

## Why SQLite

SQLite was chosen for simplicity and portability:

- no separate database server is required
- easy setup for local testing and marking
- fully compatible with SQLAlchemy ORM

It is ideal for a student backend API where the focus is API design and data handling.

## Project Structure

```text
webcwk1/
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- database.py
|   |-- models.py
|   |-- schemas.py
|   |-- crud.py
|   |-- routers/
|       |-- __init__.py
|       |-- applications.py
|-- tests/
|   |-- __init__.py
|   |-- test_applications.py
|-- requirements.txt
|-- README.md
```

## Installation

1. Clone the repository and open the project folder.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

Run the API server:

```bash
uvicorn app.main:app --reload
```

Default local URL:

- http://127.0.0.1:8000

## Swagger UI

Open interactive API documentation at:

- http://127.0.0.1:8000/docs

Alternative OpenAPI JSON:

- http://127.0.0.1:8000/openapi.json

## Running Tests

```bash
pytest -q
```

## API Documentation

Base URL: `http://127.0.0.1:8000`

### 1) Create Application

- Purpose: Create a new job application record.
- Method: POST
- URL: /applications
- Query parameters: None
- Request body:

```json
{
  "company_name": "TechNova",
  "job_title": "Junior Backend Developer",
  "application_date": "2026-04-10",
  "status": "applied",
  "interview_round": 1,
  "notes": "Revise SQL joins and API testing",
  "result": "pending"
}
```

- Example request:

```http
POST /applications HTTP/1.1
Content-Type: application/json
```

- Example JSON response:

```json
{
  "id": 1,
  "company_name": "TechNova",
  "job_title": "Junior Backend Developer",
  "application_date": "2026-04-10",
  "status": "applied",
  "interview_round": 1,
  "notes": "Revise SQL joins and API testing",
  "result": "pending",
  "created_at": "2026-04-14T10:00:00",
  "updated_at": "2026-04-14T10:00:00"
}
```

- Status codes: 201 Created, 422 Unprocessable Entity
- Error responses:
  - 422 for invalid request fields (for example missing company_name)

### 2) List All Applications

- Purpose: Return all application records.
- Method: GET
- URL: /applications
- Query parameters: None
- Request body: None
- Example request:

```http
GET /applications HTTP/1.1
```

- Example JSON response:

```json
[
  {
    "id": 2,
    "company_name": "CloudEdge",
    "job_title": "Backend Engineer",
    "application_date": "2026-04-11",
    "status": "interviewing",
    "interview_round": 2,
    "notes": "Practice system design",
    "result": "pending",
    "created_at": "2026-04-14T10:10:00",
    "updated_at": "2026-04-14T10:10:00"
  }
]
```

- Status codes: 200 OK
- Error responses: none in normal operation

### 3) Get Application by ID

- Purpose: Return one application by its ID.
- Method: GET
- URL: /applications/{application_id}
- Query parameters: None
- Request body: None
- Example request:

```http
GET /applications/1 HTTP/1.1
```

- Example JSON response:

```json
{
  "id": 1,
  "company_name": "TechNova",
  "job_title": "Junior Backend Developer",
  "application_date": "2026-04-10",
  "status": "applied",
  "interview_round": 1,
  "notes": "Revise SQL joins and API testing",
  "result": "pending",
  "created_at": "2026-04-14T10:00:00",
  "updated_at": "2026-04-14T10:00:00"
}
```

- Status codes: 200 OK, 404 Not Found
- Error responses:
  - 404 if the application ID does not exist

### 4) Update Application

- Purpose: Update one or more fields of an existing application.
- Method: PUT
- URL: /applications/{application_id}
- Query parameters: None
- Request body:

```json
{
  "status": "offer",
  "interview_round": 3,
  "result": "Offer received"
}
```

- Example request:

```http
PUT /applications/1 HTTP/1.1
Content-Type: application/json
```

- Example JSON response:

```json
{
  "id": 1,
  "company_name": "TechNova",
  "job_title": "Junior Backend Developer",
  "application_date": "2026-04-10",
  "status": "offer",
  "interview_round": 3,
  "notes": "Revise SQL joins and API testing",
  "result": "Offer received",
  "created_at": "2026-04-14T10:00:00",
  "updated_at": "2026-04-14T10:20:00"
}
```

- Status codes: 200 OK, 404 Not Found, 422 Unprocessable Entity
- Error responses:
  - 404 if the application ID does not exist
  - 422 for invalid field values

### 5) Delete Application

- Purpose: Delete an application by ID.
- Method: DELETE
- URL: /applications/{application_id}
- Query parameters: None
- Request body: None
- Example request:

```http
DELETE /applications/1 HTTP/1.1
```

- Example JSON response: No response body
- Status codes: 204 No Content, 404 Not Found
- Error responses:
  - 404 if the application ID does not exist

### 6) Filter Applications by Status

- Purpose: Return applications that match a given status.
- Method: GET
- URL: /applications/filter
- Query parameters:
  - status (required): applied | interviewing | offer | rejected | withdrawn
- Request body: None
- Example request:

```http
GET /applications/filter?status=interviewing HTTP/1.1
```

- Example JSON response:

```json
[
  {
    "id": 2,
    "company_name": "CloudEdge",
    "job_title": "Backend Engineer",
    "application_date": "2026-04-11",
    "status": "interviewing",
    "interview_round": 2,
    "notes": "Practice system design",
    "result": "pending",
    "created_at": "2026-04-14T10:10:00",
    "updated_at": "2026-04-14T10:10:00"
  }
]
```

- Status codes: 200 OK, 422 Unprocessable Entity
- Error responses:
  - 422 if status value is invalid

### 7) Search Applications

- Purpose: Search by company name or job title.
- Method: GET
- URL: /applications/search
- Query parameters:
  - keyword (required): search text
- Request body: None
- Example request:

```http
GET /applications/search?keyword=backend HTTP/1.1
```

- Example JSON response:

```json
[
  {
    "id": 2,
    "company_name": "CloudEdge",
    "job_title": "Backend Engineer",
    "application_date": "2026-04-11",
    "status": "interviewing",
    "interview_round": 2,
    "notes": "Practice system design",
    "result": "pending",
    "created_at": "2026-04-14T10:10:00",
    "updated_at": "2026-04-14T10:10:00"
  }
]
```

- Status codes: 200 OK, 400 Bad Request, 422 Unprocessable Entity
- Error responses:
  - 400 if keyword is empty after trimming spaces
  - 422 if query format is invalid

### 8) Get Summary

- Purpose: Return summary metrics for reporting and dashboard use.
- Method: GET
- URL: /applications/summary
- Query parameters: None
- Request body: None
- Example request:

```http
GET /applications/summary HTTP/1.1
```

- Example JSON response:

```json
{
  "total_applications": 3,
  "status_breakdown": {
    "applied": 1,
    "interviewing": 1,
    "offer": 1
  },
  "result_breakdown": {
    "pending": 2,
    "Offer received": 1
  },
  "average_interview_round": 2.0
}
```

- Status codes: 200 OK
- Error responses: none in normal operation
