from fastapi import HTTPException
import jwt

from temp_service.core.config import settings

ALGORITHM = "HS256"


# for testing purposes
def create_jwt_token() -> str:
    data = {"service_name": "analytic_service"}
    return jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
