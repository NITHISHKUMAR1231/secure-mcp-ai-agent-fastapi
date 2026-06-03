# app/tools/monitor_tool.py

from app.logger import app_logger

class MonitorTool:

    def execute(self):

        app_logger.info(
            "Monitor Tool Executed"
        )

        return {

            "cpu":
            "25%",

            "memory":
            "48%"
        }