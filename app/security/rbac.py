# app/security/rbac.py

from app.logger import app_logger

permissions = {

    "admin": [
        "health_tool",
        "deploy_tool",
        "monitor_tool",
        "log_tool"
    ],

    "viewer": [
        "health_tool",
        "log_tool"
    ]
}


def authorize(
    role,
    tool_name
):

    app_logger.info(
        f"RBAC Check "
        f"Role={role} "
        f"Tool={tool_name}"
    )

    if tool_name not in permissions.get(
        role,
        []
    ):

        app_logger.error(
            "RBAC Access Denied"
        )

        raise Exception(
            "Access Denied"
        )

    app_logger.info(
        "RBAC Passed"
    )