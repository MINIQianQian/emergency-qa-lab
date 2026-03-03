import uuid
import requests


def test_health_ok(base_url: str) -> None:
    r = requests.get(f"{base_url}/health", timeout=5)
    assert r.status_code == 200


def test_create_and_get_alert(base_url: str) -> None:
    unique_title = f"Test Alert {uuid.uuid4()}"

    payload = {
        "device_id": "TWX550-TEST-001",
        "reason": "manual_test",
        "title": unique_title,
        "description": "Test description",
        "severity": "HIGH",
    }

    create_resp = requests.post(f"{base_url}/alerts", json=payload, timeout=5)
    print("CREATE RESPONSE:", create_resp.status_code, create_resp.text)
    assert create_resp.status_code == 200

    data = create_resp.json()
    # assert response schema (what the API actually guarantees)
    assert data["device_id"] == payload["device_id"]
    assert data["reason"] == payload["reason"]
    assert data["status"] == "CREATED"
    assert "id" in data and isinstance(data["id"], str)
    assert "created_at" in data

    alert_id = data["id"]

    get_resp = requests.get(f"{base_url}/alerts/{alert_id}", timeout=5)
    assert get_resp.status_code == 200
    get_data = get_resp.json()

    assert get_data["id"] == alert_id
    assert get_data["device_id"] == payload["device_id"]
    assert get_data["reason"] == payload["reason"]
    assert get_data["status"] in ("CREATED", "OPEN", "ACKED", "CLOSED")


def test_get_nonexistent_alert_returns_404(base_url: str) -> None:
    fake_id = "non-existent-id"

    resp = requests.get(
        f"{base_url}/alerts/{fake_id}",
        timeout=5
    )

    assert resp.status_code == 404


def test_create_alert_validation_error_missing_device_id(base_url: str) -> None:
    payload = {
        "reason": "manual_test",
        "title": "Bad Alert",
        "description": "Missing device_id",
        "severity": "HIGH",
    }

    resp = requests.post(f"{base_url}/alerts", json=payload, timeout=5)
    assert resp.status_code == 422

    detail = resp.json()["detail"]
    assert any(d["loc"][-1] == "device_id" for d in detail)

def test_ui_homepage_accessible(base_url: str) -> None:
    r = requests.get(f"{base_url}/", timeout=5)
    assert r.status_code == 200
    assert "Emergency Alert Console" in r.text