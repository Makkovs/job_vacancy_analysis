import jwt
from fastapi import HTTPException, status
from datetime import datetime, timedelta, timezone

from config import settings
from exception import UnauthorizedError

ALGORITHM = "HS256"

def create_access_token (data: dict) -> str:
    payload = data.copy()
    exp = datetime.now(timezone.utc) + timedelta(hours=12)
    payload.update({"exp" : exp})

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_access_token(token: str) -> dict:
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    
    except jwt.ExpiredSignatureError:
        raise UnauthorizedError
    except jwt.InvalidTokenError:
        raise UnauthorizedError