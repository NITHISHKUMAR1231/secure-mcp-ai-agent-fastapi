# app/security/audit.py

from app.audit_logger import audit_logger


def audit_log(
    username,
    role,
    action,
    status
):

    audit_logger.info(
        f"USER={username} | "
        f"ROLE={role} | "
        f"ACTION={action} | "
        f"STATUS={status}"
    )