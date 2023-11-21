import os
from celery.schedules import crontab


class Config:
    PROJECT_NAME = "temperature_service"

    DATABASE_URL = os.environ.get("DATABASE_URL")
    TEST_DATABASE_URL = "sqlite:///:memory:?cache=shared"

    # celery
    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = "rpc://"
    CELERY_BEAT_SCHEDULE = {
        "fetch-temperature": {
            "task": "fetch_temperature",
            "schedule": 15,
        },
    }
    CELERY_IMPORTS = ["temp_service.services.tasks"]

    # weather api
    CITY_NAME = os.environ.get("CITY_NAME")
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

    # auth
    SECRET_KEY = os.environ.get("SECRET_KEY")


settings = Config()
