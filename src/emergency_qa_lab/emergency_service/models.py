from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AlertCreateRequest(BaseModel):
    device_id: str = Field(..., min_length=3, max_length=32)
    reason: str = Field(..., min_length=1, max_length=200)


class AlertResponse(BaseModel):
    id: str
    device_id: str
    reason: str
    status: str
    created_at: datetime
    idempotency_key: Optional[str] = None