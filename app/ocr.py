"""Utilities for extracting text from PDF documents."""
from __future__ import annotations

from pathlib import Path
from typing import List

import pdfplumber
from PIL import Image
import pytesseract

from app.config import get_settings
from app.utils.log import get_logger

logger = get_logger(__name__)


class OCRResult(dict):
    """JSON serialisable OCR log entry."""

    page_number: int
    method: str
    text_length: int


def _ocr_page_image(image: Image.Image, language: str) -> str:
    try:
        return pytesseract.image_to_string(image, lang=language)
    except pytesseract.TesseractError as exc:  # pragma: no cover - depends on system
        logger.warning("OCR failed: %s", exc)
        return ""


def extract_text(path: Path, max_pages: int | None = None, language: str | None = None) -> str:
    """Extract text from the provided PDF file.

    The function prioritises the embedded text layer, while falling back to OCR when
    necessary. OCR operations are logged to ``logs/ocr_pages.jsonl``.
    """

    if max_pages is None:
        max_pages = get_settings().max_pages
    if language is None:
        language = get_settings().language

    ocr_logs: List[OCRResult] = []
    texts: List[str] = []
    with pdfplumber.open(str(path)) as pdf:
        for index, page in enumerate(pdf.pages[:max_pages]):
            text = page.extract_text() or ""
            method = "text"
            if not text.strip():
                try:
                    page_image = page.to_image(resolution=200)
                    pil_image = page_image.original
                    text = _ocr_page_image(pil_image, language)
                    method = "ocr"
                except Exception as exc:  # pragma: no cover - fallback safety
                    logger.warning("Failed OCR for page %s: %s", index + 1, exc)
                    text = ""
                    method = "none"
            texts.append(text)
            ocr_logs.append(
                OCRResult(
                    page_number=index + 1,
                    method=method,
                    text_length=len(text),
                )
            )

    logs_path = Path(get_settings().logs_dir) / "ocr_pages.jsonl"
    logs_path.parent.mkdir(parents=True, exist_ok=True)
    with logs_path.open("a", encoding="utf-8") as file:
        for log_entry in ocr_logs:
            file.write(f"{log_entry}\n")

    return "\n".join(texts)


__all__ = ["extract_text"]
