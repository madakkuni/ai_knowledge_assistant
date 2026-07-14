import logging

from fastapi import APIRouter

logger = logging.getLogger("ai_knowledge_assistant")

router = APIRouter()


@router.get("/health")
def health():

    logger.info("Health endpoint invoked.")

    return {
        "status": "healthy"
    }