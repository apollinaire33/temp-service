from sqlalchemy import func
from sqlalchemy.orm import Session

from temp_service.api.models import TempRecord
from temp_service.db.models import TempModel


class TempService:
    _table = TempModel

    def __init__(self, session: Session) -> None:
        self.session = session
    
    def add_record(self, temp_value: float) -> TempRecord:
        record = self._table(value=temp_value)
        self.session.add(record)
        self.session.commit()
        return TempRecord.from_orm(record)

    def get_records_by_day(self, day: str) -> list[TempRecord]:
        records = self.session.query(self._table).filter(func.date(self._table.date)==day).all()
        return [TempRecord.from_orm(record) for record in records]
