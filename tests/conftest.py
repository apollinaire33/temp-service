import os

import pytest

os.environ["SECRET_KEY"] = "SECRET_KEY"
os.environ["WEATHER_API_KEY"] = "API_KEY"


@pytest.fixture
def date():
    return "1991-12-08"
