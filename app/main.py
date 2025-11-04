"""Command line interface for BidWriter Agent."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from app.config import get_settings
from app.ocr import extract_text
from app.parse import parse_rfp_text
from app.plugins import load_plugin
from app.render_docx import export_docx
from app.templates import build_tech_sections
from app.utils.io import read_text, write_json
from app.utils.log import get_logger

logger = get_logger(__name__)


def _load_rfp(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        logger.info("Extracting text from PDF via OCR/Text parsing")
        return extract_text(path)
    logger.info("Reading text file input")
    return read_text(path)


def run_cli(args: argparse.Namespace) -> dict[str, Any]:
    settings = get_settings()
    logger.info("Starting BidWriter Agent with settings: %s", settings.dict())

    rfp_path = Path(args.rfp)
    if not rfp_path.exists():
        raise FileNotFoundError(f"RFP file not found: {rfp_path}")

    text = _load_rfp(rfp_path)
    requirements = parse_rfp_text(text, use_llm=args.use_llm)

    plugin = load_plugin(args.scene)
    if plugin:
        requirements = plugin.on_requirements(requirements)
        logger.info("Plugin %s applied", plugin.name)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    parse_dir = outdir / "parse"
    parse_dir.mkdir(parents=True, exist_ok=True)

    write_json(json.loads(requirements.json()), parse_dir / "requirements.json")

    brand = args.brand or "BidWriter"
    title = args.title or rfp_path.stem

    sections = build_tech_sections(requirements, brand=brand, title=title, plugin=plugin)
    docx_path = outdir / "bid_tech_proposal.docx"
    export_docx(sections, docx_path, title=title, brand=brand)

    summary = {
        "docx_path": str(docx_path),
        "requirements_path": str(parse_dir / "requirements.json"),
        "use_llm": bool(args.use_llm),
        "scene": args.scene,
    }
    write_json(summary, parse_dir / "summary.json")
    logger.info("Generation complete: %s", summary)
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="BidWriter Agent CLI")
    parser.add_argument("--rfp", required=True, help="Path to RFP file (.pdf or .txt)")
    parser.add_argument("--outdir", default="out", help="Output directory")
    parser.add_argument("--brand", default="", help="Brand or organisation name")
    parser.add_argument("--title", default="", help="Proposal title override")
    parser.add_argument("--use-llm", action="store_true", help="Enable LLM assisted parsing")
    parser.add_argument("--scene", default=None, help="Plugin scene identifier, e.g. smart_factory")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    summary = run_cli(args)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
