"""Global exceptions for the application."""


class AppException(Exception):
    """Base exception for the application."""

    def __init__(self, detail: str, status_code: int = 500):
        self.detail = detail
        self.status_code = status_code
        super().__init__(detail)
