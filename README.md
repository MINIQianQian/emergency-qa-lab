# emergency-qa-lab

A small, enterprise-style QA lab project to practice:
- API testing (pytest + requests)
- Service under test (FastAPI + uvicorn)
- src-layout packaging (Poetry)
- (later) UI E2E (Playwright) and BDD (Behave)

## Tech Stack

- Python 3.10+
- FastAPI + Uvicorn
- Poetry (dependency & virtualenv management)
- pytest + requests (+ pytest-html)
- ruff (lint)
- Playwright (planned)
- Behave (planned)

## Project Structure


emergency-qa-lab/
src/
emergency_qa_lab/
emergency_service/
main.py
models.py
storage.py
tests/
api/
pyproject.toml
poetry.lock
README.md


## Prerequisites

- Python installed (Windows: `py --version`)
- Poetry installed (`poetry --version`)

## Setup

Install dependencies and the current project:

```powershell
cd C:\Users\Liu\projects\emergency-qa-lab
poetry install
Run the Service

Start the API server:

poetry run uvicorn emergency_qa_lab.emergency_service.main:app --reload --port 8000

Open:

Swagger UI: http://127.0.0.1:8000/docs

Health check: http://127.0.0.1:8000/health

Run Tests

(We will add API tests under tests/api.)

poetry run pytest -q

Generate an HTML report:

poetry run pytest --html=report.html --self-contained-html
Lint
poetry run ruff check .
Notes

This repo uses a src/ layout. The package is emergency_qa_lab.

GitHub remote is configured via SSH.