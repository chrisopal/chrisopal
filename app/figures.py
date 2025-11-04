"""SVG figure generation stubs."""
from __future__ import annotations

from typing import List


def build_gantt_svg(phases: List[str]) -> str:
    """Return a simple SVG placeholder for a Gantt chart."""

    width = 600
    height = 40 + 30 * len(phases)
    svg_parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}'>",
        "<style>text{font-family:Arial;font-size:14px;}</style>",
        "<rect width='100%' height='100%' fill='#f5f5f5' stroke='#d0d0d0' />",
    ]
    for index, phase in enumerate(phases):
        y = 30 + index * 30
        svg_parts.append(
            f"<rect x='50' y='{y}' width='{400 - index * 30}' height='20' fill='#4C8BF5' opacity='0.7' />"
        )
        svg_parts.append(f"<text x='60' y='{y + 15}'>{phase}</text>")
    svg_parts.append("</svg>")
    return "".join(svg_parts)


__all__ = ["build_gantt_svg"]
