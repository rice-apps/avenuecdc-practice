from fastapi import APIRouter

from app.schemas.report import GenerateReportRequest, GenerateReportResponse
from app.services.report_generator import generate_report


router = APIRouter(tags=["reports"])


@router.post("/generate-report", response_model=GenerateReportResponse)
def create_report(request: GenerateReportRequest) -> GenerateReportResponse:
    return generate_report(request)
