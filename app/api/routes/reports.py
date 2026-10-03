from fastapi import APIRouter, HTTPException

from app.schemas.report import GenerateReportRequest, GenerateReportResponse
from app.services.report_generator import (
    ReportGenerationError,
    ReportGeneratorConfigurationError,
    generate_report,
)


router = APIRouter(tags=["reports"])


@router.post("/generate-report", response_model=GenerateReportResponse)
def create_report(request: GenerateReportRequest) -> GenerateReportResponse:
    try:
        return generate_report(request)
    except ReportGeneratorConfigurationError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except ReportGenerationError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
