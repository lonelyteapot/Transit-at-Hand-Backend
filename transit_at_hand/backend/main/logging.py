import sys

from loguru import logger

from transit_at_hand.backend.main.settings import Settings


def _preformat_log(obj):
    level = obj["level"].name
    obj["mypadding"] = " " * (8 - len(level))
    return "<level>{level}</level>:{mypadding} {message}\n"


def configure_logging(settings: Settings):
    logger.configure(
        handlers=[
            {
                "sink": sys.stderr,
                "level": "DEBUG" if settings.debug else "INFO",
                "format": _preformat_log,
            }
        ]
    )
