from fastapi import FastAPI
from app.api.v1.endpoints import download, qualities
from app.config.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(download.router, prefix="/api/v1", tags=["QRCode"])
app.include_router(qualities.router, prefix="/api/v1", tags=["QRCode"])