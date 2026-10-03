from typing import Literal

from pydantic import BaseModel, ConfigDict


class TranscriptEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    speaker: str
    text: str


class GenerateReportRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    transcript: list[TranscriptEntry]


class HousingSupportReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    caller_name: str | None
    location: str | None
    housing_status: str | None
    reason_for_call: str | None
    monthly_income: float | None
    household_size: int | None
    assistance_needed: list[str]
    urgency: Literal["low", "medium", "high"] | None
    next_steps: list[str]


class GenerateReportResponse(BaseModel):
    status: Literal["success"]
    message: str
    report: HousingSupportReport | None = None
