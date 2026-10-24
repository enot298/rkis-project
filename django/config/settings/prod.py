"""Настройки для боевого сервера.

Включаются переменной окружения DJANGO_SETTINGS_MODULE=config.settings.prod.
В боевом режиме DEBUG всегда выключен, а HTTPS-защита включена.
"""
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F401,F403
from .base import ALLOWED_HOSTS, SECRET_KEY

DEBUG = False

if SECRET_KEY.startswith("dev-only"):
    raise ImproperlyConfigured("В боевом окружении нужен собственный SECRET_KEY.")
if not ALLOWED_HOSTS:
    raise ImproperlyConfigured("Задайте ALLOWED_HOSTS для боевого окружения.")

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
