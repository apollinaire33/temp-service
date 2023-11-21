from datetime import datetime

from unittest.mock import Mock
import pytest

from httpx import AsyncClient

from temp_service.api.models import TempRecord, TempRecordResponse


@pytest.fixture
def temp_records(date):
    dt = datetime.strptime(date, "%Y-%m-%d")
    return [
        TempRecord(id=1, value=123, date=dt),
        TempRecord(id=2, value=321, date=dt),
        TempRecord(id=3, value=213, date=dt),
    ]


async def test_temp_record_response(date, temp_records):
    dt = datetime.strptime(date, "%Y-%m-%d")
    assert dt.hour == TempRecordResponse(**temp_records[0].model_dump()).hour


async def test_get_records_by_day(
    mock_temp_service: Mock,
    async_api_client: AsyncClient,
    date: str,
    temp_records: list[TempRecord],
):
    mock_temp_service.get_records_by_day.return_value = temp_records

    response = await async_api_client.get(f"/temp?day={date}")
    content = response.json()

    assert response.status_code == 200
    assert content == [
        TempRecordResponse(**temp_record.model_dump()).model_dump(mode="json")
        for temp_record in temp_records
    ]
    mock_temp_service.get_records_by_day.assert_called_once_with(date)
