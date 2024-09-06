from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings




engine = create_async_engine(
    settings.DATABASE_URL_ASYNC_PSYCOPG,
    # echo = True
)



session_async = async_sessionmaker(engine)