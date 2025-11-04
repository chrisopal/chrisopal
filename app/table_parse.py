"""Placeholder for advanced table parsing of scoring rubrics."""
from __future__ import annotations

from pathlib import Path
from typing import List

from app.parse import ScoringItem


def extract_scoring_tables(pdf_path: Path) -> List[ScoringItem]:
    """Extract scoring items from tables within a PDF.

    The MVP provides a heuristic stub returning an empty list. Future iterations can
    leverage pdfplumber table detection and coordinate analysis to improve accuracy.
    """

    return []


__all__ = ["extract_scoring_tables"]
