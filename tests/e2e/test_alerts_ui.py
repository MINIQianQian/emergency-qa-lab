import json
import re
from typing import Any, Dict

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
def test_create_and_get_alert_via_ui(page: Page, base_url: str) -> None:
    # 1) open UI
    page.goto(f"{base_url}/", wait_until="domcontentloaded")
    expect(page.get_by_role("heading", name="Emergency Alert Console")).to_be_visible()

    # 2) fill form
    page.locator("#device_id").fill("TWX550-TEST-001")
    page.locator("#reason").fill("e2e_test")

    # 3) create alert
    page.locator("#btnCreate").click()

    # 4) assert create result JSON contains status CREATED and has id
    result_text = page.locator("#result").inner_text()
    data = _parse_json_block(result_text)

    assert data["device_id"] == "TWX550-TEST-001"
    assert data["reason"] == "e2e_test"
    assert data["status"] == "CREATED"
    assert "id" in data and isinstance(data["id"], str) and len(data["id"]) > 10

    alert_id = data["id"]

    # 5) click Get Alert
    page.locator("#alert_id").fill(alert_id)
    page.locator("#btnGet").click()

    # 6) assert get result has same id
    # ✅ wait until UI updates the resultGet box (avoid race)
    expect(page.locator("#resultGet")).to_contain_text('"id"', timeout=5000)
    get_text = page.locator("#resultGet").inner_text()
    data2 = _parse_json_block(get_text)

    assert data2["id"] == alert_id
    assert data2["device_id"] == "TWX550-TEST-001"
    assert data2["reason"] == "e2e_test"


def _parse_json_block(text: str) -> Dict[str, Any]:
    """
    The UI prints JSON pretty-printed in <pre>. Sometimes it may contain whitespace.
    This helper makes parsing robust and gives a clear error if not JSON.
    """
    text = text.strip()
    # quick sanity: must look like JSON object
    if not (text.startswith("{") and text.endswith("}")):
        # try to extract first {...} block if any
        m = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if m:
            text = m.group(0)
    return json.loads(text)