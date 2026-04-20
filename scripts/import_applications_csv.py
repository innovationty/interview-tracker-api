import csv
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.database import Base, SessionLocal, engine
from app.models import Application

ALLOWED_STATUSES = {"applied", "interviewing", "offer", "rejected", "withdrawn"}


def parse_date(value: str):
    return datetime.strptime(value.strip(), "%Y-%m-%d").date()


def normalize_status(value: str) -> str:
    status = value.strip().lower()
    if status not in ALLOWED_STATUSES:
        return "applied"
    return status


def import_csv(csv_path: Path) -> int:
    db = SessionLocal()
    inserted = 0

    try:
        with csv_path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                application = Application(
                    company_name=row.get("company_name", "").strip(),
                    job_title=row.get("job_title", "").strip(),
                    application_date=parse_date(row.get("application_date", "")),
                    status=normalize_status(row.get("status", "applied")),
                    interview_round=int(row.get("interview_round", "0")),
                    notes=(row.get("notes") or "").strip() or None,
                    result=(row.get("result") or "pending").strip() or "pending",
                )

                # Skip rows that are clearly incomplete.
                if not application.company_name or not application.job_title:
                    continue

                db.add(application)
                inserted += 1

        db.commit()
        return inserted
    finally:
        db.close()


def main():
    csv_path = Path("data/job_applications_seed.csv")
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    Base.metadata.create_all(bind=engine)
    inserted_count = import_csv(csv_path)
    print(f"Imported {inserted_count} records from {csv_path}")


if __name__ == "__main__":
    main()
