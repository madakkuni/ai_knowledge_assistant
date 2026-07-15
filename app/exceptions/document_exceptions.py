class DocumentLoadException(Exception):
    """Raised when a document cannot be loaded."""

    def __init__(self, message: str):
        super().__init__(message)