from pathlib import Path

from app.parse import parse_rfp_text


def test_parse_sample_rfp_scope_and_scoring():
    text = Path("sample_data/sample_rfp.txt").read_text(encoding="utf-8")
    requirements = parse_rfp_text(text)
    assert requirements.scope
    assert requirements.scoring.total >= 40
    assert requirements.constraints.lines
