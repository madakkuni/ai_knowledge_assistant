import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.document_exceptions import DocumentLoadException

logger = logging.getLogger("ai_knowledge_assistant")


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(DocumentLoadException)
    async def document_load_exception_handler(request: Request, exc: DocumentLoadException):

        logger.error(str(exc))

        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc)
            }
        )