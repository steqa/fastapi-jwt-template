from datetime import timedelta, datetime, UTC
from uuid import uuid4

import jwt

from api.settings import settings
from api.user.schemas import SUser

ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"


def create_access_token(user: SUser) -> str:
    jwt_payload = {
        "type": ACCESS_TOKEN_TYPE,
        "id": str(user.id),
    }
    return encode_jwt(
        payload=jwt_payload,
        expire_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )


def create_refresh_token(user: SUser) -> str:
    jwt_payload = {
        "type": REFRESH_TOKEN_TYPE,
        "sub": str(user.id),
        "jti": str(uuid4()),
    }
    return encode_jwt(
        payload=jwt_payload,
        expire_timedelta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
    )


def encode_jwt(
        payload: dict,
        private_key: str = settings.JWT_PRIVATE_KEY,
        algorithm: str = settings.JWT_ALGORITHM,
        expire_minutes: int = settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.now(UTC)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
    )

    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.JWT_PUBLIC_KEY,
        algorithm: str = settings.JWT_ALGORITHM,
) -> dict:
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded
