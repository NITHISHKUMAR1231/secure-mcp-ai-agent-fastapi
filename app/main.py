# app/main.py

from fastapi import FastAPI
from fastapi import Depends
from fastapi import Request

from fastapi.security import (
    OAuth2PasswordRequestForm
)

import jwt

from app.agent import AIAgent

from app.security.auth import (
    verify_token
)

from app.security.rate_limit import (
    limiter
)

from app.logger import app_logger

SECRET_KEY = "mysecretkey"

app = FastAPI()

agent = AIAgent()


@app.post("/login")
def login(
    form_data:
    OAuth2PasswordRequestForm
    = Depends()
):

    role = "viewer"

    if (
        form_data.username
        == "admin"
    ):
        role = "admin"

    payload = {

        "username":
        form_data.username,

        "role":
        role
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    app_logger.info(
        f"User Login: "
        f"{form_data.username}"
    )

    return {

        "access_token":
        token,

        "token_type":
        "bearer"
    }


@app.get("/agent/{task}")
@limiter.limit("10/minute")
def run_agent(
    request: Request,
    task: str,
    user=Depends(
        verify_token
    )
):

    try:

        result = (
            agent.process_request(
                task,
                user
            )
        )

        return {

            "status":
            "success",

            "data":
            result
        }

    except Exception as e:

        app_logger.error(
            str(e)
        )

        return {

            "status":
            "error",

            "message":
            str(e)
        }