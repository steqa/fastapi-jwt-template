from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.dependencies import get_current_auth_user
from api.auth.schemas import SUserPayload
from api.database import get_session
from api.user import services as user_services
from api.user.schemas import SUserCreate, SUserResponse

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
):
    user = await user_services.create_user(
        db=session,
        username=user.username,
        password=user.password
    )
    return user


# ──────────────────────────────────── Get ────────────────────────────────────
@router.get("/me", response_model=SUserResponse)
async def get_current_user(
        user: SUserPayload = Depends(get_current_auth_user),
        session: AsyncSession = Depends(get_session),
):
    user = await user_services.get_user(
        db=session,
        id_=user.id
    )
    return user
