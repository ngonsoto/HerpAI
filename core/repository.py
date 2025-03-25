# .herpai/ingestion/core/data/repository/base.py
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Generic, TypeVar, Type
from sqlalchemy.future import select

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session = session
        self.model = model

    async def get(self, id: Any) -> Optional[T]:
        result = await self.session.execute(
            select(self.model).filter(self.model.id == id)
        )
        return result.scalars().first()

    async def create(self, **kwargs) -> T:
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        return instance

