from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.root import router as root_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.exceptions.handlers import register_exception_handlers
from app.api.documents import router as document_router

logger = setup_logging()

logger.info("==============================================")
logger.info("Starting AI Knowledge Assistant")
logger.info("Environment : %s", settings.environment)
logger.info("Version     : %s", settings.app_version)
logger.info("==============================================")

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)
register_exception_handlers(app)


app.include_router(root_router)
app.include_router(health_router)
app.include_router(document_router)