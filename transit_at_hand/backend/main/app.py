from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from loguru import logger

from transit_at_hand.backend.main.settings import get_settings

from .logging import configure_logging


def create_app():
    settings = get_settings()
    configure_logging(settings)

    if settings.debug:
        logger.warning("Running in debug mode.")

    return FastAPI(
        debug=settings.debug,
        title=settings.app_title,
        description=settings.app_description,
        version=settings.app_version,
    )


app = create_app()


@app.get("/", response_class=RedirectResponse)
def home():
    return app.docs_url or "/docs"
