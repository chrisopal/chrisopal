from pathlib import Path

from fastapi.testclient import TestClient

from app.api import app


def test_full_endpoint_returns_success():
    client = TestClient(app)
    text = Path("sample_data/sample_rfp.txt").read_text(encoding="utf-8")
    response = client.post(
        "/v1/full",
        json={"rfp_text": text, "brand": "Example", "title": "Sample", "use_llm": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert "docx_path" in data
    assert Path(data["docx_path"]).exists()
