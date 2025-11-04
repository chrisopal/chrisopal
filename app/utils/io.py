"""Input/Output helper functions."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_text(path: Path) -> str:
    """Read text content from a file."""

    return path.read_text(encoding="utf-8")


def write_json(data: Any, path: Path) -> None:
    """Write JSON data to the target path."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_binary(content: bytes, path: Path) -> None:
    """Write binary content to disk."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


__all__ = ["read_text", "write_json", "write_binary"]
