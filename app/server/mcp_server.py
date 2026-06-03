# app/server/mcp_server.py

from app.registry.tool_registry import get_all_tools

from app.llm.llm_router import detect_tool

from app.security.rbac import authorize

from app.security.prompt_guard import (
    validate_prompt
)

from app.exceptions import (
    ToolNotFoundException
)

from app.logger import app_logger


class MCPServer:

    def process_request(
        self,
        task,
        user
    ):

        app_logger.info(
            f"MCP Server Received: {task}"
        )

        validate_prompt(task)

        selected_tool = detect_tool(
            task
        )

        app_logger.info(
            f"Selected Tool: "
            f"{selected_tool}"
        )

        authorize(
            user["role"],
            selected_tool
        )

        tools = get_all_tools()

        if selected_tool not in tools:

            app_logger.error(
                "Tool Not Found"
            )

            raise ToolNotFoundException(
                "Tool not found"
            )

        result = (
            tools[selected_tool]
            .execute()
        )

        return result