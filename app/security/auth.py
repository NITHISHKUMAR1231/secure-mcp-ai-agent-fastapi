# app/security/auth.py

import jwt

from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from app.logger import app_logger

SECRET_KEY = "mysecretkey"

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def verify_token(
    token: str = Depends(
        oauth2_scheme
    )
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        app_logger.info(
            f"JWT Verified "
            f"{payload['username']}"
        )

        return payload

    except Exception:

        app_logger.error(
            "Invalid JWT"
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )