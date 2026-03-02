import logging
from fastapi import FastAPI, Header, HTTPException

from .models import AlertCreateRequest, AlertResponse
from .storage import InMemoryAlertStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("emergency_service")

app = FastAPI(title="Emergency Alert Service")
store = InMemoryAlertStore()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/alerts", response_model=AlertResponse)
def create_alert(
    payload: AlertCreateRequest,
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
):
    logger.info("Creating alert for device %s", payload.device_id)

    alert = store.create_alert(
        device_id=payload.device_id,
        reason=payload.reason,
        idempotency_key=idempotency_key,
    )

    # dataclass -> dict 让 FastAPI 返回 JSON + response_model 校验
    return AlertResponse(**alert.__dict__)


@app.get("/alerts/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: str):
    alert = store.get_alert(alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    return AlertResponse(**alert.__dict__)