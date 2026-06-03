# app/agent.py

from app.client.mcp_client import (
    MCPClient
)

from app.security.audit import (
    audit_log
)

from app.logger import app_logger


class AIAgent:

    def __init__(self):

        self.client = MCPClient()

    def process_request(
        self,
        task,
        user
    ):

        try:

            app_logger.info(
                f"Agent Processing "
                f"{task}"
            )

            result = (
                self.client
                .send_request(
                    task,
                    user
                )
            )

            audit_log(
                user["username"],
                user["role"],
                task,
                "SUCCESS"
            )

            return result

        except Exception as e:

            audit_log(
                user["username"],
                user["role"],
                task,
                "FAILED"
            )

            raise e