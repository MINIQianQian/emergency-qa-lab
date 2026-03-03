FROM python:3.11-slim

WORKDIR /app

# system deps for healthcheck curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first (better cache)
COPY pyproject.toml poetry.lock* /app/

# Install Poetry + deps (no venv inside container)
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy source
COPY . /app

EXPOSE 8000

# IMPORTANT: make src/ importable
ENV PYTHONPATH=/app/src

# Start FastAPI
CMD ["uvicorn", "emergency_qa_lab.emergency_service.main:app", "--host", "0.0.0.0", "--port", "8000"]