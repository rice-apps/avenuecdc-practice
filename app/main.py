from fastapi import FastAPI

from app.api.routes.reports import router as reports_router


app = FastAPI(title="Housing Support Report API")
app.include_router(reports_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Housing Support Report API"}
