"""Plugin system for BidWriter Agent."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Protocol

from app.parse import Requirements


class BasePlugin(Protocol):
    """Minimal interface plugins must implement."""

    name: str

    def on_requirements(self, requirements: Requirements) -> Requirements:
        ...

    def terms(self) -> List[str]:
        ...

    def kpis(self) -> List[str]:
        ...

    def risks(self) -> List[str]:
        ...

    def summary(self, requirements: Requirements) -> str:
        ...


@dataclass
class PluginConfig:
    """Store plugin registration metadata."""

    name: str
    plugin: BasePlugin


def load_plugin(scene: Optional[str]) -> Optional[BasePlugin]:
    """Load plugin by scene identifier."""

    if scene is None:
        return None
    scene = scene.lower()
    if scene == "smart_factory":
        from app.plugins.smart_factory import SmartFactoryPlugin

        return SmartFactoryPlugin()
    return None


__all__ = ["BasePlugin", "PluginConfig", "load_plugin"]
