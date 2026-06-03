# app/registry/tool_registry.py

from app.tools.health_tool import HealthTool
from app.tools.deploy_tool import DeployTool
from app.tools.monitor_tool import MonitorTool
from app.tools.log_tool import LogTool


def get_all_tools():

    return {

        "health_tool":
        HealthTool(),

        "deploy_tool":
        DeployTool(),

        "monitor_tool":
        MonitorTool(),

        "log_tool":
        LogTool()
    }