import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import ApplicationException
from app.models.error_response import ErrorDetail, ErrorResponse

logger = logging.getLogger("ai_knowledge_assistant")


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(ApplicationException)
    async def application_exception_handler(
        request: Request,
        exc: ApplicationException,
    ):

        logger.exception(exc.message)

        response = ErrorResponse(
            error=ErrorDetail(
                code=exc.code,
                message=exc.message,
            )
        )

        return JSONResponse(
            status_code=400,
            content=response.model_dump(),
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):

        logger.exception("Unhandled exception")

        response = ErrorResponse(
            error=ErrorDetail(
                code="INTERNAL_SERVER_ERROR",
                message="Unexpected error occurred.",
            )
        )

        return JSONResponse(
            status_code=500,
            content=response.model_dump(),
        )