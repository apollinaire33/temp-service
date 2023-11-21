from unittest.mock import patch
import pytest

from httpx import AsyncClient

from temp_service.core.dependencies import get_temp_service, verify_token


@pytest.fixture
def mock_temp_service():
    with patch("temp_service.services.temp_service.TempService") as mock:
        return mock


@pytest.fixture()
def app(mock_temp_service):
    from temp_service.main import app

    app.dependency_overrides[get_temp_service] = lambda: mock_temp_service
    app.dependency_overrides[verify_token] = lambda: {}
    return app


@pytest.fixture()
async def async_api_client(app):
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
