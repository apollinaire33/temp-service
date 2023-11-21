from datetime import datetime

from pydantic import BaseModel, ConfigDict, validator


class TempRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    value: float
    date: datetime


class TempRecordResponse(TempRecord):
    hour: int = None

    @validator("hour", pre=True, always=True)
    def calculate_hour(cls, v, values) -> int:
        return v or values.get("date").hour
