from fastapi import Depends, Header, HTTPException

from temp_service.db.setup_db import get_db
from temp_service.services.auth import decode_jwt_token
from temp_service.services.temp_service import TempService


async def get_temp_service(session = Depends(get_db)) -> TempService:
    return TempService(session)


def verify_token(x_token: str = Header(None)) -> dict:
    if x_token is None:
        raise HTTPException(status_code=401, detail="Token is missing")
    return decode_jwt_token(x_token)
