from abc import ABC, abstractmethod

from sqlalchemy import insert, select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import BaseSchema


class AbstractRepository(ABC):
    @abstractmethod
    async def create_one(self, session: AsyncSession, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_first(self, session: AsyncSession, filters: list = None):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, session: AsyncSession, filters: list = None):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def create_one(
            self,
            session: AsyncSession,
            data: dict
    ) -> BaseSchema:
        query = insert(self.model).values(**data).returning(self.model)
        result = await session.execute(query)
        await session.commit()
        return result.scalars().one().to_schema()

    async def get_first(
            self,
            session: AsyncSession,
            filters: list = None
    ) -> BaseSchema | None:
        query = select(self.model)
        if filters:
            query = query.where(and_(*filters))
        result = await session.execute(query)
        row = result.scalars().first()
        return row.to_schema() if row else None

    async def get_all(
            self, session: AsyncSession,
            filters: list = None
    ) -> list[BaseSchema]:
        query = select(self.model)
        if filters:
            query = query.where(and_(*filters))
        result = await session.execute(query)
        return [row.to_schema() for row in result.scalars().all()]
