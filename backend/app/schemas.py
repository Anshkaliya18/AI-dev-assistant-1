"""Pydantic request / response models for QyverixAI."""

from __future__ import annotations
<<<<<<< HEAD
from typing import Any, List
from pydantic import BaseModel, field_validator


class CodeRequest(BaseModel):
    code: str
    language: str | None = None

    @field_validator("code")
    class HealthResponse(BaseModel):
    def code_must_not_be_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("code must not be empty")
    # ── Share ────────────────────────────────────────────────────────────────────
    class ShareCreateRequest(BaseModel):
        code: str
        result: Any


    class ShareCreateResponse(BaseModel):
        id: str


    class ShareRecord(BaseModel):
        id: str
        code: str
        result: Any
        created_at: str


    # ── History & Favorites ───────────────────────────────────────────────────────
    class HistoryRecord(BaseModel):
        id: int
        action: str
        code: str
        result_json: dict | None = None
        created_at: str


    class HistoryCreateRequest(BaseModel):
        action: str
        code: str
        result_json: dict | None = None


    class FavoriteRecord(BaseModel):
        id: int
        title: str
        action: str
        code: str
        result_json: dict | None = None
        created_at: str


    class FavoriteCreateRequest(BaseModel):
        title: str
        action: str
        code: str
        result_json: dict | None = None


    # ── Progress Tracking ─────────────────────────────────────────────────────────
    class AnalysisProgressPoint(BaseModel):
        id: int
        score: float
        errors_count: int
        language: str
        created_at: str


    class ProgressDashboardResponse(BaseModel):
        history: List[AnalysisProgressPoint]
        average_score: float
        best_score: float
        most_improved: float
    analysis_time_ms: float | None = None


# ── Weekly Digest / Subscription ───────────────────────────────────────────────
class SubscribeRequest(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def email_must_be_valid(cls, v: str) -> str:
        v = v.strip().lower()
        if "@" not in v or "." not in v.split("@")[-1]:
            raise ValueError("Invalid email address")
        if len(v) > 320:
            raise ValueError("Email too long")
        return v


class SubscribeResponse(BaseModel):
    message: str
    email: str


class UnsubscribeRequest(BaseModel):
    email: str
    token: str


# ── Health ────────────────────────────────────────────────────────────────────
class HealthResponse(BaseModel):
    status: str
    version: str
    message: str
    endpoints: list[str] | None = None


<<<<<<< HEAD
# ── Share ────────────────────────────────────────────────────────────────────
class ShareCreateRequest(BaseModel):
    code: str
    result: Any


class ShareCreateResponse(BaseModel):
    id: str


class ShareRecord(BaseModel):
    id: str
    code: str
    result: Any
    created_at: str
=======
# ── History & Favorites ───────────────────────────────────────────────────────
class HistoryRecord(BaseModel):
    id: int
    action: str
    code: str
    result_json: dict | None = None
    created_at: str


class HistoryCreateRequest(BaseModel):
    action: str
    code: str
    result_json: dict | None = None


class FavoriteRecord(BaseModel):
    id: int
    title: str
    action: str
    code: str
    result_json: dict | None = None
    created_at: str


class FavoriteCreateRequest(BaseModel):
    title: str
    action: str
    code: str
    result_json: dict | None = None


# ── Progress Tracking ─────────────────────────────────────────────────────────
class AnalysisProgressPoint(BaseModel):
    id: int
    score: float
    errors_count: int
    language: str
    created_at: str


class ProgressDashboardResponse(BaseModel):
    history: List[AnalysisProgressPoint]
    average_score: float
    best_score: float
    most_improved: float
>>>>>>> 33d9406eee8e84ee4582feb8826d148092b64e94
