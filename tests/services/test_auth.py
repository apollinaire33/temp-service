import pytest

from fastapi import HTTPException

from temp_service.services.auth import decode_jwt_token


async def test_decode_jwt_token(token: str):
    assert decode_jwt_token(token) == {"service_name": "analytic_service"}


async def test_decode_jwt_token_401():
    with pytest.raises(HTTPException):
        decode_jwt_token("BLABLABLA")
