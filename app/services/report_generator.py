from app.schemas.report import GenerateReportRequest, GenerateReportResponse


def generate_report(request: GenerateReportRequest) -> GenerateReportResponse:
    """Return a placeholder until transcript parsing is implemented."""
    return GenerateReportResponse(
        status="success",
        message=f"Transcript received with {len(request.transcript)} entries.",
        report=None,
    )
