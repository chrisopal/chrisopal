"""Logging utilities."""
from __future__ import annotations

import logging
from pathlib import Path

from app.config import get_settings

_LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging() -> None:
    """Configure the root logger once."""

    logging.basicConfig(level=logging.INFO, format=_LOG_FORMAT)
    settings = get_settings()
    logs_dir = Path(settings.logs_dir)
    logs_dir.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    """Get a configured logger."""

    configure_logging()
    return logging.getLogger(name)


__all__ = ["get_logger", "configure_logging"]
