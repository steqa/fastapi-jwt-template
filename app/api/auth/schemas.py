from uuid import UUID

from api.schemas import BaseSchema


class STokenResponse(BaseSchema):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"


class SUserPayload(BaseSchema):
    id: UUID
