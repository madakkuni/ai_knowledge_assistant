from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.root import router as root_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)

app.include_router(root_router)
app.include_router(health_router)