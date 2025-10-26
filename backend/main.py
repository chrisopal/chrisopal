from __future__ import annotations

import json
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .data.word_sets import WORD_SETS

BASE_DIR = Path(__file__).resolve().parent
STATE_PATH = BASE_DIR / "state.json"


class AnswerRecord(BaseModel):
    questionId: str = Field(..., alias="questionId")
    wordId: str = Field(..., alias="wordId")
    selected: str
    correct: bool
    type: str


class ProgressPayload(BaseModel):
    date: str
    answers: List[AnswerRecord]
    total: int


class FavoritePayload(BaseModel):
    word_id: str = Field(..., alias="word_id")
    favorite: bool


app = FastAPI(title="词海日程 API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
    ,
    allow_headers=["*"],
)


def read_state() -> Dict:
    if not STATE_PATH.exists():
        STATE_PATH.write_text(json.dumps({
            "config": {"difficulty": "junior", "words_per_day": 10},
            "history": {},
            "favorites": [],
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def write_state(state: Dict) -> None:
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def find_word(word_id: str) -> Optional[Dict]:
    for difficulty_words in WORD_SETS.values():
        for word in difficulty_words:
            if word["id"] == word_id:
                return word
    return None


def ensure_start_date(state: Dict) -> None:
    if "start_date" not in state:
        state["start_date"] = date.today().isoformat()


def get_dataset(difficulty: str) -> List[Dict]:
    if difficulty not in WORD_SETS:
        raise HTTPException(status_code=400, detail="Unsupported difficulty level")
    return WORD_SETS[difficulty]


def slice_words(dataset: List[Dict], start: int, count: int) -> List[Dict]:
    if not dataset:
        return []
    result = []
    for offset in range(count):
        index = (start + offset) % len(dataset)
        result.append(dataset[index])
    return result


def build_quiz_items(words: List[Dict]) -> List[Dict]:
    quiz_items: List[Dict] = []
    for word in words:
        if not word.get("questions"):
            continue
        question = word["questions"][0]
        quiz_items.append(
            {
                "id": f"{word['id']}-{question['type']}",
                "wordId": word["id"],
                "term": word["term"],
                "type": question["type"],
                "prompt": question["prompt"],
                "options": question.get("options", []),
                "answer": question["answer"],
                "passage": question.get("passage"),
            }
        )
    return quiz_items


def collect_words_by_ids(word_ids: List[str]) -> List[Dict]:
    words: List[Dict] = []
    for word_id in word_ids:
        word = find_word(word_id)
        if word:
            words.append(word)
    return words


def summarise_answers(answers: List[AnswerRecord]) -> Dict:
    total = len(answers)
    mistakes = [answer for answer in answers if not answer.correct]
    mistake_words: List[str] = []
    seen = set()
    for answer in mistakes:
        if answer.wordId not in seen:
            seen.add(answer.wordId)
            mistake_words.append(answer.wordId)
    accuracy = round((total - len(mistakes)) / total * 100) if total else 0
    focus_types: Dict[str, int] = {}
    for answer in mistakes:
        focus_types[answer.type] = focus_types.get(answer.type, 0) + 1
    breakdown = {}
    for answer in mistakes:
        breakdown.setdefault(answer.wordId, 0)
        breakdown[answer.wordId] += 1
    suggestions: List[str] = []
    if mistakes:
        suggestions.append(
            f"建议重点复习 {len(mistake_words)} 个未掌握词汇，尤其关注 {', '.join(mistake_words[:3])}。"
        )
    if focus_types:
        type_labels = {
            "multiple_choice": "选择题",
            "cloze": "完形填空",
            "reading": "阅读理解",
        }
        top_types = ", ".join(type_labels.get(tp, tp) for tp in focus_types.keys())
        suggestions.append(f"加强 {top_types} 题型训练，提升精准度。")
    if not suggestions:
        suggestions.append("表现优秀，保持复习节奏巩固记忆。")
    return {
        "accuracy": accuracy,
        "mistakes": [answer.dict(by_alias=True) for answer in mistakes],
        "mistake_words": mistake_words,
        "analysis_text": " ".join(suggestions),
        "breakdown": breakdown,
    }


@app.get("/api/config")
def get_config():
    state = read_state()
    ensure_start_date(state)
    write_state(state)
    favorites = state.get("favorites", [])
    return {
        "config": state["config"],
        "favorites": favorites,
        "today": date.today().isoformat(),
        "difficulty": state["config"].get("difficulty"),
    }


@app.post("/api/config")
def update_config(payload: Dict):
    state = read_state()
    config = state.get("config", {})
    difficulty = payload.get("difficulty", config.get("difficulty", "junior"))
    words_per_day = int(payload.get("words_per_day", config.get("words_per_day", 10)))
    if difficulty not in WORD_SETS:
        raise HTTPException(status_code=400, detail="非法难度选项")
    if not 5 <= words_per_day <= 30:
        raise HTTPException(status_code=400, detail="每日单词量需在 5-30 之间")
    config.update({"difficulty": difficulty, "words_per_day": words_per_day})
    state["config"] = config
    ensure_start_date(state)
    write_state(state)
    return {"config": config}


@app.get("/api/words")
def get_words(date: str = Query(default=date.today().isoformat())):
    state = read_state()
    ensure_start_date(state)
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="日期格式错误，应为 YYYY-MM-DD") from exc

    config = state["config"]
    dataset = get_dataset(config["difficulty"])

    start_date = datetime.strptime(state["start_date"], "%Y-%m-%d").date()
    day_offset = max((target_date - start_date).days, 0)
    words_per_day = config.get("words_per_day", 10)
    start_index = day_offset * words_per_day

    new_words = slice_words(dataset, start_index, words_per_day)

    previous_day = (target_date - timedelta(days=1)).isoformat()
    review_ids = state.get("history", {}).get(previous_day, {}).get("mistake_words", [])
    review_words = collect_words_by_ids(review_ids)

    quiz_items = build_quiz_items(new_words + review_words)
    favorites = state.get("favorites", [])
    favorite_ids = [item["id"] for item in favorites]

    return {
        "date": date,
        "difficulty": config["difficulty"],
        "new_words": new_words,
        "review_words": review_words,
        "quiz_items": quiz_items,
        "favorites": favorite_ids,
        "favorite_words": favorites,
        "default_mastered": state.get("history", {}).get(date, {}).get("mastered", []),
    }


@app.post("/api/progress")
def update_progress(payload: ProgressPayload):
    state = read_state()
    ensure_start_date(state)
    try:
        datetime.strptime(payload.date, "%Y-%m-%d")
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="日期格式错误，应为 YYYY-MM-DD") from exc

    summary = summarise_answers(payload.answers)
    history = state.setdefault("history", {})
    history[payload.date] = {
        "answers": [answer.dict(by_alias=True) for answer in payload.answers],
        "total": payload.total,
        "accuracy": summary["accuracy"],
        "mistake_words": summary["mistake_words"],
        "analysis": summary["analysis_text"],
        "mastered": [answer.wordId for answer in payload.answers if answer.correct],
    }
    state["history"] = history

    # Update favorites to include frequently incorrect words
    favorite_set = {fav["id"] for fav in state.get("favorites", [])}
    for word_id in summary["mistake_words"]:
        if word_id not in favorite_set:
            word = find_word(word_id)
            if word:
                state.setdefault("favorites", []).append(word)
    write_state(state)

    stats = {
        "learned_words": payload.total,
        "mistake_words": len(summary["mistake_words"]),
        "review_words": len(summary["mistake_words"]),
        "ai_analysis": summary["analysis_text"],
    }

    return {
        "status": "ok",
        "stats": stats,
        "review_words": collect_words_by_ids(summary["mistake_words"]),
        "favorites": state.get("favorites", []),
    }


@app.post("/api/favorite")
def toggle_favorite(payload: FavoritePayload):
    state = read_state()
    favorites = state.setdefault("favorites", [])
    existing_ids = {item["id"] for item in favorites}

    if payload.favorite:
        if payload.word_id not in existing_ids:
            word = find_word(payload.word_id)
            if not word:
                raise HTTPException(status_code=404, detail="未找到对应单词")
            favorites.append(word)
    else:
        favorites = [item for item in favorites if item["id"] != payload.word_id]
        state["favorites"] = favorites

    write_state(state)
    return {"favorites": favorites}


@app.get("/api/stats")
def get_stats(date: str = Query(default=date.today().isoformat())):
    state = read_state()
    history = state.get("history", {})
    record = history.get(date)
    if not record:
        return {
            "learned_words": 0,
            "mistake_words": 0,
            "review_words": 0,
            "ai_analysis": "今日暂无学习记录，请完成测验后查看智能分析。",
        }
    return {
        "learned_words": record.get("total", 0),
        "mistake_words": len(record.get("mistake_words", [])),
        "review_words": len(record.get("mistake_words", [])),
        "ai_analysis": record.get("analysis", "保持复习节奏，巩固记忆。"),
    }
