# app/client/mcp_client.py

from app.server.mcp_server import (
    MCPServer
)

from app.logger import app_logger


class MCPClient:

    def __init__(self):

        self.server = MCPServer()

    def send_request(
        self,
        task,
        user
    ):

        app_logger.info(
            "MCP Client Sending Request"
        )

        return (
            self.server
            .process_request(
                task,
                user
            )
        )