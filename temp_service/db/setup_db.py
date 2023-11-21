from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from temp_service.core.config import settings

Base = declarative_base()
engine = create_engine(settings.DATABASE_URL, echo=False)
session = sessionmaker(engine, expire_on_commit=False)


def get_db() -> None:
    with session() as s:
        yield s
