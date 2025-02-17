from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad request"

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail
        )
