# app/tools/log_tool.py

from app.logger import app_logger

class LogTool:

    def execute(self):

        app_logger.info(
            "Log Tool Executed"
        )

        return {

            "logs":
            "Application Running Successfully"
        }