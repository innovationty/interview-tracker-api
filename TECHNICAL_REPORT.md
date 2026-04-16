# Technical Report

## Project Title
Job Application and Interview Preparation Tracker API

## 1. Introduction

This technical report presents the design and implementation of the **Job Application and Interview Preparation Tracker API**, developed as an undergraduate coursework project for web services and web data. The purpose of the project is to provide a backend-only REST API that allows users to manage job application records in a structured way.

Many students and graduates apply to multiple roles at the same time. During this process, they need to track company names, job titles, interview progress, notes, and outcomes. Without a system, this information is often scattered across notebooks or spreadsheets. This project addresses that issue by creating a clear, simple API that stores and manages these records consistently.

From an academic perspective, the project demonstrates core backend skills expected at undergraduate level:

- API design using REST principles
- CRUD (Create, Read, Update, Delete) operations
- SQL database integration
- request validation and structured JSON responses
- error handling with suitable HTTP status codes
- endpoint testing and maintainable project structure

The project is intentionally kept simple and realistic. It avoids unnecessary enterprise-level complexity and focuses on correctness, clarity, and explainability, which are important for coursework assessment, technical reporting, and oral presentation.

## 2. System Overview

The system is a backend-only web API built with FastAPI. It exposes endpoints to create and manage application records and includes extra endpoints for filtering, searching, and summary statistics.

At a high level, the architecture is divided into clear modules:

- **Router layer**: defines HTTP endpoints and response models.
- **CRUD layer**: contains database logic and query operations.
- **Schema layer**: defines request/response data contracts using Pydantic.
- **Model layer**: defines SQLAlchemy ORM entities mapped to SQL tables.
- **Database layer**: configures engine, sessions, and base class.

This modular design makes the code easier to read and explain in a viva. Each file has one clear responsibility, reducing confusion and improving maintainability.

The API supports the following practical workflow:

1. Create job application records.
2. List all applications.
3. Retrieve one application by ID.
4. Update statuses and interview rounds.
5. Delete records when needed.
6. Filter applications by status.
7. Search applications by company or role title.
8. View summary metrics for progress tracking.

## 3. Technology Stack and Justification

### 3.1 FastAPI

FastAPI was selected as the primary web framework for several reasons:

- It has a clean and modern Python style.
- It integrates naturally with Pydantic for validation.
- It automatically generates OpenAPI documentation.
- It provides Swagger UI (`/docs`) for easy demonstration.

For coursework, FastAPI is particularly suitable because it allows students to build a working API quickly while still following good engineering practices. In oral presentation, endpoints and schema definitions can be explained clearly without heavy boilerplate code.

### 3.2 SQLite

SQLite was chosen as the project database because:

- it requires no separate server installation,
- setup is simple for local development and marking,
- it is sufficient for small to medium coursework datasets,
- it works smoothly with SQLAlchemy.

For an undergraduate project, SQLite reduces operational overhead and allows more focus on API logic, data modeling, and testing.

### 3.3 SQLAlchemy ORM

SQLAlchemy ORM provides a clear mapping between Python classes and SQL tables. This improves readability and avoids writing raw SQL for basic operations. ORM usage also aligns with coursework requirements for SQL database integration.

### 3.4 Pydantic

Pydantic schemas are used to validate input data and define output structures. This ensures:

- invalid data is rejected early,
- API responses are consistent,
- route contracts are explicit and easy to document.

### 3.5 Testing Tools

Pytest and FastAPI TestClient are used to test API behavior. This verifies endpoint correctness and supports reproducible evidence in the technical report.

## 4. API Design

The API follows resource-oriented REST principles using JSON requests and responses. The main resource is **Application**.

### 4.1 Endpoint Summary

- `POST /applications` - Create an application.
- `GET /applications` - List all applications.
- `GET /applications/{application_id}` - Get one application by ID.
- `PUT /applications/{application_id}` - Update application details.
- `DELETE /applications/{application_id}` - Delete an application.
- `GET /applications/filter?status=...` - Filter by status.
- `GET /applications/search?keyword=...` - Search by company name or job title.
- `GET /applications/summary` - Return summary statistics.

### 4.2 Design Considerations

The endpoint design was kept explicit and beginner-friendly:

- CRUD operations are represented by standard HTTP methods.
- Query endpoints (`filter`, `search`) are separated for clarity.
- The `summary` endpoint provides useful aggregate information for reports.

### 4.3 Documentation Support

Each route includes summary and description metadata. Combined with FastAPI’s automatic OpenAPI generation, this enables high-quality interactive documentation through Swagger UI (`/docs`).

This is useful for:

- demonstrating endpoint usage to markers,
- validating request/response formats,
- supporting oral presentation with live examples.

## 5. Database Design

The core table is `applications`, mapped from the `Application` SQLAlchemy model.

### 5.1 Application Model Fields

- `id` (Integer, primary key): unique record identifier.
- `company_name` (String): target company name.
- `job_title` (String): role title applied for.
- `application_date` (Date): date of application submission.
- `status` (String): application stage, e.g., `applied`, `interviewing`, `offer`, `rejected`, `withdrawn`.
- `interview_round` (Integer): interview stage index (0, 1, 2, ...).
- `notes` (Text, optional): preparation notes and observations.
- `result` (String, optional): outcome text, default `pending`.
- `created_at` (DateTime): creation timestamp.
- `updated_at` (DateTime): modification timestamp.

### 5.2 Rationale

The model design is intentionally simple but practical:

- It captures essential data for job tracking.
- It supports all required CRUD operations.
- It enables filtering (`status`), search (`company_name`, `job_title`), and summary statistics (`status_breakdown`, `average_interview_round`).

The structure balances realism with coursework scope, avoiding unnecessary complexity.

## 6. Validation and Error Handling

Validation is handled through Pydantic schemas.

### 6.1 Request Validation

Examples of validation rules include:

- required text fields for company and job title,
- constrained status values,
- interview round range constraints,
- optional notes and result fields with length limits.

If a request fails schema validation, FastAPI returns `422 Unprocessable Entity` automatically.

### 6.2 Error Handling Strategy

The API uses clear HTTP exceptions for common failure cases:

- `404 Not Found` when an application ID does not exist,
- `400 Bad Request` for invalid search input (e.g., blank keyword after trimming),
- `422 Unprocessable Entity` for invalid query/body formats.

This approach makes behavior predictable and easy to explain in an assessment.

## 7. Testing Approach

Testing is implemented with pytest and FastAPI TestClient. The tests use a dedicated SQLite test database and reset the schema before each test to ensure independent, repeatable results.

### 7.1 Covered Scenarios

The test suite covers:

- creating an application record,
- listing all records,
- retrieving a single record,
- updating a record,
- deleting a record,
- filtering by status,
- searching by company name/job title,
- summary endpoint correctness,
- missing record handling (`404`).

### 7.2 Academic Value

These tests provide objective evidence that the API satisfies functional requirements. They also demonstrate good software engineering practice expected in university submissions.

## 8. Challenges Encountered

During development, several practical challenges were encountered:

1. **Model evolution and consistency**: Field names changed during refinement (for example, from preparation-progress style naming to `interview_round` and `result`). This required synchronized updates to schemas, CRUD logic, routes, tests, and README.
2. **Route design clarity**: There was an initial decision point between combined query filtering and separate dedicated endpoints. Separate endpoints (`/filter`, `/search`) were selected because they are easier for beginners to understand and demonstrate.
3. **Documentation alignment**: Keeping documentation exactly aligned with implementation required careful checking. Mismatched examples can reduce report quality, so this was corrected.
4. **Validation edge cases**: Search input needed explicit handling for blank strings after trimming spaces, which was resolved with a `400` response.

## 9. Limitations and Future Improvements

The project meets coursework requirements, but some limitations remain.

### 9.1 Current Limitations

- Single-user API; no authentication or user accounts.
- SQLite is suitable for coursework but not ideal for high-concurrency production workloads.
- No pagination for very large datasets.
- Basic summary metrics only.

### 9.2 Small and Realistic Future Improvements

The following improvements are intentionally modest and still appropriate for undergraduate scope:

- Add pagination (`page`, `page_size`) to `GET /applications`.
- Add sort options (e.g., by `application_date` or `created_at`).
- Add simple status transition validation (optional business rule checks).
- Add one export endpoint for CSV summary output.
- Extend tests with a few more negative cases.

These improvements can increase quality without introducing enterprise complexity.

## 10. Conclusion

The Job Application and Interview Preparation Tracker API successfully demonstrates the key outcomes of a web services coursework project. It implements a complete backend API with:

- a clear data model,
- full CRUD operations,
- filtering, search, and summary endpoints,
- SQL database integration,
- validation and structured error handling,
- automated tests and interactive documentation.

The use of FastAPI, SQLite, SQLAlchemy, and Pydantic creates a strong balance between technical quality and simplicity. The final system is practical, explainable, and suitable for technical reporting, live API demonstration, and oral assessment.

## 11. Generative AI Declaration

This project was developed with support from generative AI tools for drafting code structure, documentation drafts, and testing templates. All generated content was reviewed, edited, and validated by the student.

The student takes full responsibility for:

- final design decisions,
- code correctness,
- testing and validation,
- documentation accuracy,
- compliance with coursework requirements and academic integrity policies.

AI assistance was used as a productivity and learning aid, not as a replacement for understanding or independent verification.
