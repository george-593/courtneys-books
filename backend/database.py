from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings

engine = create_async_engine(settings.database_url)

SessionLocal = async_sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
