from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.dependencies import get_current_auth_user
from api.auth.schemas import SUserPayload
from api.database import get_session
from api.user.dependencies import user_service as user_service_dependency
from api.user.schemas import SUserCreate, SUserResponse
from api.user.service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])


# ────────────────────────────────── Create ───────────────────────────────────
@router.post(
    "",
    response_model=SUserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
        user: SUserCreate,
        session: AsyncSession = Depends(get_session),
        user_service: UserService = Depends(user_service_dependency),
):
    user = await user_service.create_user(session=session, user=user)
    return user


# ──────────────────────────────────── Get ────────────────────────────────────
@router.get("/me", response_model=SUserResponse)
async def get_current_user(
        user: SUserPayload = Depends(get_current_auth_user),
        session: AsyncSession = Depends(get_session),
        user_service: UserService = Depends(user_service_dependency),
):
    user = await user_service.get_user(session=session, id_=user.id)
    return user
