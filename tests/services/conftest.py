from datetime import datetime

from freezegun import freeze_time
from unittest.mock import patch, Mock
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from temp_service.api.models import TempRecord
from temp_service.core.config import settings
from temp_service.db.base import metadata
from temp_service.services.auth import create_jwt_token
from temp_service.services.temp_service import TempService

test_engine = create_engine(settings.TEST_DATABASE_URL)

session_local = sessionmaker(test_engine, expire_on_commit=False)


@pytest.fixture
def datetime_date(date):
    return datetime.strptime(date, "%Y-%m-%d")


@pytest.fixture
def temp_record(datetime_date):
    return TempRecord(
        id=1,
        value=27,
        date=datetime_date,
    )


@pytest.fixture
def token():
    return create_jwt_token()


@pytest.fixture
def test_session():
    connection = test_engine.connect()
    transaction = connection.begin()
    session = session_local(bind=connection)

    yield session

    session.rollback()
    transaction.rollback()
    connection.close()


@pytest.fixture(autouse=True, scope="session")
def prepare_database():
    metadata.create_all(test_engine)
    yield
    metadata.drop_all(test_engine)


@pytest.fixture
def temp_service_class(test_session):
    return TempService(test_session)


@pytest.fixture
def temp_db_record(date, temp_service_class, temp_record):
    with freeze_time(date):
        return temp_service_class.add_record(temp_record.value)


@pytest.fixture
def mock_httpx_client():
    with patch("httpx.Client") as mock_client_manager:
        mock_client = Mock()
        mock_client_manager.return_value.__enter__.return_value = mock_client
        yield mock_client
