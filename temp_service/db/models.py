import datetime

from sqlalchemy import Column, Float, DateTime, Integer

from temp_service.db.setup_db import Base


class TempModel(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    value = Column(Float, nullable=False)
    date = Column(DateTime, default=lambda: datetime.datetime.now(), nullable=False)
