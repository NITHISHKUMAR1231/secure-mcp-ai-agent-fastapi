# app/audit_logger.py

import logging

audit_logger = logging.getLogger(
    "audit_logger"
)

audit_logger.setLevel(
    logging.INFO
)

handler = logging.FileHandler(
    "audit.log"
)

formatter = logging.Formatter(
    "%(asctime)s - %(message)s"
)

handler.setFormatter(
    formatter
)

audit_logger.addHandler(
    handler
)