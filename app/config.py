"""Application configuration management using Pydantic settings."""
from __future__ import annotations

from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Runtime configuration loaded from environment variables."""

    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-5-thinking", env="OPENAI_MODEL")
    max_pages: int = Field(default=50, env="MAX_PAGES")
    language: str = Field(default="zh", env="LANG")
    target_score: int = Field(default=92, env="TARGET_SCORE")
    logs_dir: str = Field(default="logs", env="LOGS_DIR")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a singleton settings object."""

    return Settings()


__all__ = ["Settings", "get_settings"]
