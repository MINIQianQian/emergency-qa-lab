import os
import pytest

@pytest.fixture(scope="session")
def base_url() -> str:
    """
    Base URL of the running service under test.
    You can override:
      PowerShell: $env:BASE_URL="http://127.0.0.1:8000"
    """
    return os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")