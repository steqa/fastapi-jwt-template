from fastapi import status

from api.exceptions import BaseHTTPException


class EUsernameExists(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Username already exists"


class EInvalidUsernameOrPassword(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid username or password"


class EUserNotFound(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User not found"
