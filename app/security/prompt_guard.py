# app/security/prompt_guard.py

from app.logger import app_logger

blocked_words = [

    "delete database",

    "drop table",

    "shutdown server",

    "ignore instructions",

    "remove all users"
]


def validate_prompt(task):

    task = task.lower()

    for word in blocked_words:

        if word in task:

            app_logger.error(
                f"Prompt Injection "
                f"Detected: {task}"
            )

            raise Exception(
                "Unsafe Prompt"
            )

    app_logger.info(
        "Prompt Validation Passed"
    )