# app/llm/llm_router.py

from groq import Groq

from app.logger import app_logger

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)


def fallback_router(task):

    task = task.lower()

    if "health" in task:
        return "health_tool"

    if "deploy" in task:
        return "deploy_tool"

    if "monitor" in task:
        return "monitor_tool"

    if "log" in task:
        return "log_tool"

    return None


def detect_tool(task):

    try:

        prompt = f"""
Available Tools:

health_tool
deploy_tool
monitor_tool
log_tool

User Request:
{task}

Return only tool name.
"""

        response = (
            client.chat.completions.create(
                model="llama-3.3-70b-versatile",

                messages=[
                    {
                        "role":
                        "user",

                        "content":
                        prompt
                    }
                ]
            )
        )

        tool = (
            response
            .choices[0]
            .message.content
            .strip()
        )

        app_logger.info(
            f"Groq Selected: {tool}"
        )

        return tool

    except Exception as e:

        app_logger.error(
            f"Groq Failed: {e}"
        )

        app_logger.info(
            "Using Fallback Router"
        )

        return fallback_router(task)