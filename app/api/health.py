import logging

from fastapi import APIRouter

from app.models.health_response import HealthResponse
from app.services.health_service import HealthService

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
)
def health() -> HealthResponse:

    logger.info("Health endpoint invoked.")

    return HealthService.check()