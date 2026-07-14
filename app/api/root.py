import logging

from fastapi import APIRouter

logger = logging.getLogger("ai_knowledge_assistant")

router = APIRouter()


@router.get("/")
def root():

    logger.info("Root endpoint invoked.")

    return {
        "message": "Welcome to AI Knowledge Assistant API"
    }