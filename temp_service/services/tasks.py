import httpx

from celery import shared_task

from temp_service.core.config import settings
from temp_service.db.setup_db import session
from temp_service.services.temp_service import TempService

URL = f"https://api.openweathermap.org/data/2.5/weather?q={settings.CITY_NAME}&units=metric&appid={settings.WEATHER_API_KEY}"


@shared_task(
    name="fetch_temperature",
    autoretry_for=(httpx.HTTPError,),
    max_retries=3,
    retry_backoff=True,
)
def send_fetch_temperature() -> None:
    with httpx.Client() as client:
        response = client.get(URL)

    temp_value = response.json()["main"]["temp"]
    with session() as s:
        TempService(s).add_record(temp_value)
