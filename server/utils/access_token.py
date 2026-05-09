import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "jobsmecret"
ALGORITHM = "HS256"

def create_access_token (data: dict) -> str:
    payload = data.copy()
    exp = datetime.now(timezone.utc) + timedelta(hours=12)
    payload.update({"exp" : exp})

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_access_token(token: str) -> dict | None:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded
    
    except jwt.ExpiredSignatureError:
        return None
    
    except jwt.InvalidTokenError:
        return None