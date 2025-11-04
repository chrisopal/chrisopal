from pathlib import Path

from app.parse import parse_rfp_text
from app.render_docx import export_docx
from app.templates import build_tech_sections


def test_docx_generation(tmp_path):
    text = Path("sample_data/sample_rfp.txt").read_text(encoding="utf-8")
    requirements = parse_rfp_text(text)
    sections = build_tech_sections(requirements, brand="Example", title="Sample RFP")
    output = tmp_path / "proposal.docx"
    export_docx(sections, output, title="Sample RFP", brand="Example")
    assert output.exists()
    assert output.stat().st_size > 10 * 1024
