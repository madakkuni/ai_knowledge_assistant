class ApplicationException(Exception):
    """Base exception for the application."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(message)


class HealthCheckException(ApplicationException):
    def __init__(self):
        super().__init__(
            code="HEALTH_CHECK_FAILED",
            message="Health check failed."
        )