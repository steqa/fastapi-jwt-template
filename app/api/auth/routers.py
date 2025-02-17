from fastapi import Depends, APIRouter, status

from api.auth.dependencies import (
    get_current_auth_user_for_refresh,
    get_token_payload,
)
from api.auth.exceptions import ETokenInvalid
from api.auth.redis_services import add_token_to_blacklist
from api.auth.schemas import STokenResponse
from api.auth.utils import create_access_token, create_refresh_token
from api.user.dependencies import authenticate_user
from api.user.models import User

router = APIRouter(prefix="/api/v1/auth/jwt", tags=["auth/jwt"])


@router.post("/login", response_model=STokenResponse)
async def login_user(
        user: User = Depends(authenticate_user)
):
    return STokenResponse(
        access_token=create_access_token(user),
        refresh_token=create_refresh_token(user)
    )


@router.post(
    "/refresh",
    response_model=STokenResponse,
    description="Required refresh token",
)
async def refresh_token(
        user: User = Depends(get_current_auth_user_for_refresh),
):
    return STokenResponse(
        access_token=create_access_token(user)
    )


@router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Required refresh token",
)
async def logout_user(
        user: User = Depends(get_current_auth_user_for_refresh),
        token_payload: dict = Depends(get_token_payload)
):
    jti = token_payload.get("jti", None)
    exp = token_payload.get("exp", None)
    if jti is None or exp is None:
        raise ETokenInvalid
    add_token_to_blacklist(jti=str(jti), expire_at=str(exp))
