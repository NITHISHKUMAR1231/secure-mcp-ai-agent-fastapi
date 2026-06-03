# app/tools/health_tool.py

from app.logger import app_logger

class HealthTool:

    def execute(self):

        app_logger.info(
            "Health Tool Executed"
        )

        return {

            "service":
            "API",

            "status":
            "UP"
        }