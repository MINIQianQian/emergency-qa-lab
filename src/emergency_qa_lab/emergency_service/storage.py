from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional
import uuid


@dataclass
class Alert:
    id: str
    device_id: str
    reason: str
    status: str
    created_at: datetime
    idempotency_key: Optional[str] = None


class InMemoryAlertStore:
    def __init__(self):
        self._alerts: Dict[str, Alert] = {}
        self._idempotency_map: Dict[str, str] = {}

    def create_alert(self, device_id: str, reason: str, idempotency_key: Optional[str]):
        if idempotency_key and idempotency_key in self._idempotency_map:
            existing_id = self._idempotency_map[idempotency_key]
            return self._alerts[existing_id]

        alert_id = str(uuid.uuid4())
        alert = Alert(
            id=alert_id,
            device_id=device_id,
            reason=reason,
            status="CREATED",
            created_at=datetime.utcnow(),
            idempotency_key=idempotency_key,
        )
        self._alerts[alert_id] = alert

        if idempotency_key:
            self._idempotency_map[idempotency_key] = alert_id

        return alert

    def get_alert(self, alert_id: str):
        return self._alerts.get(alert_id)