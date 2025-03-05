import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from config import settings
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    url=settings.DB_URL,
    echo=False, 
    pool_size=5,
    max_overflow=10,
    pool_recycle=1800,
    pool_pre_ping=True
)

session_local = sessionmaker(
    engine, 
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False
)

async def test_query():
    async with engine.connect() as conn:
        async with conn.begin():
            result = await conn.execute(text("SELECT VERSION()"))  
            print(result.scalar())
            
#asyncio.run(test_query())

