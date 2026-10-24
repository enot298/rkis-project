"""Настройки для разработки (используются по умолчанию в manage.py)."""
from .base import *  # noqa: F401,F403
from .base import env_bool

DEBUG = env_bool("DEBUG", default=True)
