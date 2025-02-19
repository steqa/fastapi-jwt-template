from typing import Type
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from api.repository import AbstractRepository
from api.user.exceptions import EUserNotFound, EUsernameExists
from api.user.models import User
from api.user.schemas import SUserCreate, SUser
from api.user.utils import encrypt_password


class UserService:
    def __init__(self, user_repository: Type[AbstractRepository]):
        self.user_repository = user_repository()

    async def create_user(
            self,
            session: AsyncSession,
            user: SUserCreate
    ) -> SUser:
        existing_user = await self.get_user_or_none(
            session, username=user.username)
        if existing_user is not None:
            raise EUsernameExists

        hashed_password = encrypt_password(user.password)
        user_dict = user.model_dump()
        user_dict["password"] = hashed_password
        new_user = await self.user_repository.create_one(session, user_dict)
        return new_user

    async def get_user(
            self,
            session: AsyncSession,
            id_: UUID | None = None,
            username: str | None = None
    ) -> SUser:
        filters = []
        if id_ is not None:
            filters.append(User.id == id_)
        if username is not None:
            filters.append(User.username == username)

        user = await self.user_repository.get_first(session, filters)
        if user is None:
            raise EUserNotFound

        return user

    async def get_user_or_none(
            self,
            session: AsyncSession,
            id_: UUID | None = None,
            username: str | None = None
    ) -> SUser | None:
        filters = []
        if id_ is not None:
            filters.append(User.id == id_)
        if username is not None:
            filters.append(User.username == username)

        return await self.user_repository.get_first(session, filters)

    async def get_users(
            self,
            session: AsyncSession
    ) -> list[SUser]:
        users = await self.user_repository.get_all(session)
        return users
