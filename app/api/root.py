from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/")
def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "Running",
        "environment": settings.environment,
    }