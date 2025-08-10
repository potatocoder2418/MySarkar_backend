from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.config import settings

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode["exp"] = expire
    return jwt.encode(
        to_encode, settings.SESSION_SECRET, algorithm=settings.ALGORITHM
    )

def verify_token(token: str):
    try:
        return jwt.decode(
            token, settings.SESSION_SECRET, algorithms=[settings.ALGORITHM]
        )
    except JWTError:
        return None
