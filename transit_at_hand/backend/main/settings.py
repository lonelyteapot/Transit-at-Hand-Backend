from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Transit at Hand"
    app_description: str = ""
    app_version: str = "0.0.1"
    debug: bool = False


@lru_cache()
def get_settings():
    return Settings()
