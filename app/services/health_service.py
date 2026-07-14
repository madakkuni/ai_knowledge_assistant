from app.core.config import settings
from app.models.health_response import HealthResponse


class HealthService:

    @staticmethod
    def check() -> HealthResponse:

        return HealthResponse(
            status="healthy",
            service=settings.app_name,
            version=settings.app_version,
            environment=settings.environment,
        )