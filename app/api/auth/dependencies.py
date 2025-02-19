from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.exceptions import ETokenInvalid
from api.auth.redis_services import is_token_blacklisted
from api.auth.schemas import SUserPayload
from api.auth.utils import decode_jwt, REFRESH_TOKEN_TYPE, ACCESS_TOKEN_TYPE
from api.database import get_session
from api.user.dependencies import user_service as user_service_dependency
from api.user.schemas import SUser
from api.user.service import UserService

http_bearer = HTTPBearer()


def get_token_payload(
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> dict:
    try:
        token = credentials.credentials
        payload = decode_jwt(token=token)
    except InvalidTokenError:
        raise ETokenInvalid
    return payload


async def get_user_from_payload(payload: dict) -> SUserPayload:
    return SUserPayload(**payload)


async def get_user_by_token_sub(
        payload: dict,
        session: AsyncSession,
        user_service: UserService,
) -> SUser:
    user = await user_service.get_user(
        session=session,
        id_=payload["sub"]
    )
    return user


def validate_token_type(payload: dict, token_type: str) -> bool:
    if payload.get("type", '') == token_type:
        return True
    else:
        raise ETokenInvalid


def validate_token_blacklist(payload: dict) -> bool:
    if is_token_blacklisted(payload.get("jti", '')):
        raise ETokenInvalid
    return True


async def get_current_auth_user(
        token_payload: dict = Depends(get_token_payload),
) -> SUserPayload:
    validate_token_type(token_payload, ACCESS_TOKEN_TYPE)
    return await get_user_from_payload(token_payload)


async def get_current_auth_user_for_refresh(
        token_payload: dict = Depends(get_token_payload),
        session: AsyncSession = Depends(get_session),
        user_service: UserService = Depends(user_service_dependency),
) -> SUser:
    validate_token_type(token_payload, REFRESH_TOKEN_TYPE)
    validate_token_blacklist(token_payload)
    return await get_user_by_token_sub(token_payload, session, user_service)
