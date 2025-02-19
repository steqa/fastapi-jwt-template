from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_session
from api.user import utils
from api.user.exceptions import EInvalidUsernameOrPassword
from api.user.repository import UserRepository
from api.user.schemas import SUserLogin, SUser
from api.user.service import UserService


def user_service():
    return UserService(UserRepository)


async def authenticate_user(
        user_data: SUserLogin,
        session: AsyncSession = Depends(get_session),
        service: UserService = Depends(user_service),
) -> SUser:
    user = await service.get_user_or_none(
        session=session,
        username=user_data.username
    )
    if not user:
        raise EInvalidUsernameOrPassword
    if not utils.verify_password(user_data.password, user.password):
        raise EInvalidUsernameOrPassword
    return user
