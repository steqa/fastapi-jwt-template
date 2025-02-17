from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.user.models import User
from api.user.utils import encrypt_password


# ────────────────────────────────── Create ───────────────────────────────────
async def create_user(
        *,
        db: AsyncSession,
        username: str,
        password: str
) -> User:
    hashed_password = encrypt_password(password)
    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    await db.commit()
    return new_user


# ──────────────────────────────────── GET ────────────────────────────────────
async def get_user(
        *,
        db: AsyncSession,
        id_: UUID | None = None,
        username: str | None = None
) -> User | None:
    query = select(User)
    if id_ is not None:
        query = query.where(User.id == id_)
    if username is not None:
        query = query.where(User.username == username)
    user = await db.execute(query)
    return user.scalars().first()


async def get_users(
        *,
        db: AsyncSession
) -> list[User]:
    query = select(User)
    users = await db.execute(query)
    return list(users.scalars().all())
