from unittest.mock import Mock, patch

import httpx

from temp_service.services.tasks import send_fetch_temperature, URL


@patch("temp_service.services.tasks.TempService.add_record")
def test_send_fetch_temperature(mock_temp_service__add_record, mock_httpx_client):
    content = {"main": {"temp": 123}}
    mock_httpx_client.get = Mock(return_value=httpx.Response(200, json=content))

    send_fetch_temperature.apply().get()

    mock_httpx_client.get.assert_called_once_with(URL)
    mock_temp_service__add_record.assert_called_once_with(123)
