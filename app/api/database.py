from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from api.settings import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{settings.POSTGRES_USERNAME}:"
    f"{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

async_session = async_sessionmaker(engine, class_=AsyncSession,
                                   expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
