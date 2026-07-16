import logging
import sys
from datetime import datetime
from pathlib import Path

from app.core.config import settings

APP_LOGGER_NAME = "ai_knowledge_assistant"


def setup_logging() -> logging.Logger:
    """
    Configure application logging.
    """

    # Create log directory automatically
    log_directory = Path(settings.log_directory)
    log_directory.mkdir(parents=True, exist_ok=True)

    # Daily log filename
    log_filename = (
        f"{APP_LOGGER_NAME}_"
        f"{datetime.now().strftime('%d_%b_%Y').upper()}.log"
    )

    log_file = log_directory / log_filename

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(module)s.%(funcName)s:%(lineno)d | "
            "%(message)s"
        ),
        datefmt="%d-%m-%Y %H:%M:%S",
    )

    file_handler = logging.FileHandler(
        filename=log_file,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()

    root_logger.setLevel(settings.log_level)

    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    return logging.getLogger(APP_LOGGER_NAME)