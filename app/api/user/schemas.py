from uuid import UUID

from pydantic import Field, field_validator

from api.schemas import BaseSchema


class SUser(BaseSchema):
    id: UUID
    username: str
    password: bytes


class SUserCreate(BaseSchema):
    username: str = Field(..., min_length=5, max_length=255)
    password: str = Field(..., min_length=5, max_length=255)

    @field_validator("password")
    def validate_password(cls, value) -> str:
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isalpha() for char in value):
            raise ValueError("Password must contain at least one letter")
        if not any(char in "!@#$%^&*()-_=+" for char in value):
            raise ValueError((
                "Password must contain at least one"
                "special character (!@#$%^&*()-_=+)"
            ))
        return value


class SUserLogin(BaseSchema):
    username: str
    password: str


class SUserResponse(BaseSchema):
    id: UUID
    username: str
