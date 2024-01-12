from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from src.model import Base

from sqlalchemy.ext.asyncio import create_async_engine

class Database:

    def __init__(self) -> None:
        self._engine = create_async_engine(
            "postgresql+asyncpg://postgres:secret@database:5432/postgres", 
            echo=False, 
            future=True
        )
        
    async def close(self):
        await self._engine.close()
        
    async def create_database(self):
        async with self._engine.begin() as conn: 
            await conn.run_sync(Base.metadata.create_all)
        
    async def remove_database(self):
        async with self._engine.begin() as conn: 
            await conn.run_sync(Base.metadata.drop_all)
        
    def session_maker(self):
         return sessionmaker(self._engine, class_=AsyncSession)

    @asynccontextmanager
    async def session(self) -> AsyncSession:
        try:
            async_session = self.session_maker() 
            
            async with async_session() as session:
                yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
