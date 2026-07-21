"""
Bad Request Exception.
"""


class BadRequestException(Exception):
    """
    Raised when the client sends an invalid request.
    """

    def __init__(self, message: str):
        super().__init__(message)