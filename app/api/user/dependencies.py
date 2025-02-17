from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_session
from api.user import services as user_services, utils
from api.user.exceptions import EInvalidUsernameOrPassword
from api.user.models import User
from api.user.schemas import SUserLogin


async def authenticate_user(
        user_data: SUserLogin,
        session: AsyncSession = Depends(get_session)
) -> User:
    user = await user_services.get_user(
        db=session,
        username=user_data.username
    )
    if not user:
        raise EInvalidUsernameOrPassword
    if not utils.verify_password(user_data.password, user.password):
        raise EInvalidUsernameOrPassword
    return user
