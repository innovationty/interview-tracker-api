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

## Data Source and Licensing

This coursework project uses a small seed CSV file for local demonstration:

- data/job_applications_seed.csv

The seed file is educational sample data for testing the API flow. For assessed submissions that require public datasets, the same import workflow can be used with a dataset from:

- Kaggle: https://www.kaggle.com/datasets
- data.gov.uk: https://www.data.gov.uk/
- Google Dataset Search: https://datasetsearch.research.google.com/

Always verify dataset license terms and cite the dataset source in your technical report.

## AI-Assisted Dataset Workflow

Generative AI can support a simple workflow:

1. Identify a relevant public dataset.
2. Inspect columns and clean fields.
3. Map columns to the Application model fields.
4. Use the import script to load rows into SQLite.
5. Validate imported results via Swagger UI and tests.

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
|-- data/
|   |-- job_applications_seed.csv
|-- scripts/
|   |-- import_applications_csv.py
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

## Deployment

The current PythonAnywhere deployment flow is documented in [PYTHONANYWHERE_DEPLOYMENT.md](PYTHONANYWHERE_DEPLOYMENT.md). It uses the experimental `pa website create` ASGI command that matches the live deployment setup.

## Import Seed Data

The repository includes a professional seed dataset with **50 job application records** from leading technology companies (Google, Microsoft, Amazon, Apple, Netflix, Tesla, IBM, Oracle, Spotify, and others).

Run the CSV import script to load the dataset:

```bash
python scripts/import_applications_csv.py
```

Output:
```
Imported 49 records from data\job_applications_seed.csv
```

**Dataset Coverage:**
- **49 job applications** from top global tech companies
- **Status distribution**: 12 applied, 20 interviewing, 10 offers, 9 rejected, 6 withdrawn
- **Interview progression**: Records with 0-4 interview rounds
- **Realistic scenarios**: Phone screens, coding assessments, system design rounds, offers, and rejections

The import script uses the AI-assisted workflow pattern:
1. **Source identification**: Professional dataset covering major tech companies
2. **Format inspection**: CSV with company_name, job_title, application_date, status, interview_round, notes, result
3. **Schema mapping**: Python script maps CSV columns to Application ORM model fields
4. **Batch import**: Database transaction handles all 50 records with validation
5. **Outcome verification**: SQL query confirms all records persisted successfully

## API Documentation

Primary API documentation is available in two formats:

- Live Swagger UI: `http://127.0.0.1:8000/docs`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

For coursework submission, export the API docs to PDF and place the file in this repository.
Recommended filename:

- `API_DOCUMENTATION.pdf`

Then add its repository link in your technical report submission section.

## Submission Checklist (Coursework 1)

- Public GitHub repository with visible commit history
- Runnable source code matching the presented version
- README with setup, run, and docs links
- API documentation file (PDF) referenced from README/report
- Technical report with GenAI declaration
- Presentation slides for oral exam
- Optional deployment URL and demonstration evidence
