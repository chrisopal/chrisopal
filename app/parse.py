"""RFP parsing logic combining rule-based heuristics and optional LLM support."""
from __future__ import annotations

import json
import re
from typing import List, Optional

from pydantic import BaseModel, ValidationError

from app.config import get_settings
from app.utils.log import get_logger

logger = get_logger(__name__)


class ScoringItem(BaseModel):
    name: Optional[str] = None
    score: Optional[int] = None
    detail: Optional[str] = None
    line: Optional[str] = None


class Scoring(BaseModel):
    items: List[ScoringItem] = []
    total: int = 0


class Constraints(BaseModel):
    lines: List[str] = []
    banned_terms: List[str] = []
    must_have: List[str] = []
    disqualify_rules: List[str] = []


class Requirements(BaseModel):
    scope: str
    scoring: Scoring
    constraints: Constraints
    sections: List[str] = []


SYSTEM_PROMPT = (
    "你是资深招投标与政府采购专家。把输入 RFP 文本解析为 JSON，字段：\n"
    "- scope: 300字内项目/采购范围\n"
    "- scoring: { total:int, items:[{name, score, detail, line}] }\n"
    "- constraints: { banned_terms[], must_have[], disqualify_rules[], lines[] }\n"
    "- terms: 行业术语词表（最多20个）\n"
    "必须返回严格 JSON，不要解释文字。若不确定用 null。"
)

_SECTION_PATTERN = re.compile(r"^(第?[一二三四五六七八九十]+章|[一二三四五六七八九十]+、|Chapter|\d+\.\d*)", re.IGNORECASE)
_SCORE_KEYWORDS = ["评分", "分值", "分", "权重", "技术", "实施", "资质", "服务", "价格", "团队"]
_CONSTRAINT_KEYWORDS = ["不得", "必须", "应当", "严禁", "否决", "废标", "强制", "限制", "资格"]


def _clean_lines(text: str) -> List[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def _extract_sections(text: str) -> List[str]:
    lines = _clean_lines(text)
    sections: List[str] = []
    buffer: List[str] = []
    current_title = "概述"
    for line in lines:
        if _SECTION_PATTERN.match(line) and len(line) < 100:
            if buffer:
                sections.append(f"{current_title}\n" + "\n".join(buffer))
            current_title = line
            buffer = []
        else:
            buffer.append(line)
    if buffer:
        sections.append(f"{current_title}\n" + "\n".join(buffer))
    return sections


def _parse_scope(text: str) -> str:
    lines = _clean_lines(text)
    scope_lines: List[str] = []
    for line in lines[:50]:
        if any(keyword in line for keyword in ["范围", "目标", "概述", "建设"]):
            scope_lines.append(line)
        if len("".join(scope_lines)) > 600:
            break
    if not scope_lines:
        scope_lines = lines[:10]
    return "\n".join(scope_lines)[:600]


def _parse_scoring(text: str) -> Scoring:
    lines = _clean_lines(text)
    items: List[ScoringItem] = []
    total = 0
    score_regex = re.compile(r"(?P<score>\d{1,3})\s*分")
    for line in lines:
        if any(keyword in line for keyword in _SCORE_KEYWORDS) and "分" in line:
            match = score_regex.search(line)
            score = int(match.group("score")) if match else None
            items.append(
                ScoringItem(
                    name=line.split("：")[0][:60] if "：" in line else None,
                    score=score,
                    detail=line[:200],
                    line=line,
                )
            )
            if score:
                total = max(total, score)
    if total == 0 and items:
        total = sum(item.score or 0 for item in items)
    return Scoring(items=items, total=total)


def _parse_constraints(text: str) -> Constraints:
    lines = _clean_lines(text)
    hits = [line for line in lines if any(keyword in line for keyword in _CONSTRAINT_KEYWORDS)]
    banned_terms = [line for line in hits if "不得" in line or "严禁" in line]
    must_have = [line for line in hits if "必须" in line or "应当" in line]
    disqualify = [line for line in hits if "否决" in line or "废标" in line]
    return Constraints(
        lines=hits,
        banned_terms=banned_terms,
        must_have=must_have,
        disqualify_rules=disqualify,
    )


def _call_llm(text: str) -> Optional[Requirements]:
    settings = get_settings()
    if not settings.openai_api_key:
        return None
    try:
        import openai

        openai.api_key = settings.openai_api_key
        response = openai.ChatCompletion.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text[:15000]},
            ],
            temperature=0,
        )
        message = response["choices"][0]["message"]["content"]
        payload = json.loads(message)
        return Requirements(
            scope=payload.get("scope", ""),
            scoring=Scoring.parse_obj(payload.get("scoring", {})),
            constraints=Constraints.parse_obj(payload.get("constraints", {})),
            sections=payload.get("sections", []),
        )
    except (KeyError, IndexError, json.JSONDecodeError, ValidationError) as exc:
        logger.warning("LLM parsing failed: %s", exc)
        return None
    except Exception as exc:  # pragma: no cover - network or API errors
        logger.warning("LLM request failed: %s", exc)
        return None


def parse_rfp_text(text: str, use_llm: bool = False) -> Requirements:
    """Parse the given RFP text into structured requirements."""

    if use_llm:
        llm_result = _call_llm(text)
        if llm_result:
            logger.info("LLM parsing succeeded")
            return llm_result
        logger.info("Falling back to rule-based parsing")

    scope = _parse_scope(text)
    scoring = _parse_scoring(text)
    constraints = _parse_constraints(text)
    sections = _extract_sections(text)
    return Requirements(scope=scope, scoring=scoring, constraints=constraints, sections=sections)


__all__ = [
    "ScoringItem",
    "Scoring",
    "Constraints",
    "Requirements",
    "parse_rfp_text",
]
