from fastapi import APIRouter, Depends

from temp_service.api.models import TempRecordResponse
from temp_service.core.dependencies import get_temp_service, verify_token
from temp_service.services.temp_service import TempService

temp_service_router = APIRouter(prefix="/temp")


@temp_service_router.get("", response_model=list[TempRecordResponse])
async def get_records_by_day(
    day: str, temp_service: TempService = Depends(get_temp_service),
    token: dict = Depends(verify_token),
):
    records = temp_service.get_records_by_day(day)
    return records
