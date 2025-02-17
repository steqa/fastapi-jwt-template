from fastapi import status

from api.exceptions import BaseHTTPException


class ETokenInvalid(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token invalid"


class EPasswordInvalid(BaseHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Password invalid"
