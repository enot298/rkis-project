"""Общие настройки Django для всех окружений.

Конфигурация берётся из переменных окружения (файл .env, шаблон — .env.example).
Отличия разработки и боевого сервера вынесены в dev.py и prod.py.
"""
import os
from pathlib import Path

import dj_database_url
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

# django/ — корневая папка Django-проекта (там лежат manage.py и .env)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


def env(name, default=None, required=False):
    """Прочитать переменную окружения или объяснить, что делать."""
    value = os.environ.get(name, default)
    if required and value in (None, ""):
        raise ImproperlyConfigured(
            f"Не задана переменная окружения {name}. "
            "Скопируйте .env.example в .env и заполните её."
        )
    return value


def env_bool(name, default=False):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in ("1", "true", "yes", "on")


def env_list(name, default=""):
    raw = os.environ.get(name, default)
    return [item.strip() for item in raw.split(",") if item.strip()]


SECRET_KEY = env("SECRET_KEY", required=True)
DEBUG = env_bool("DEBUG", default=False)
ALLOWED_HOSTS = env_list("ALLOWED_HOSTS", "127.0.0.1,localhost")
CSRF_TRUSTED_ORIGINS = env_list("CSRF_TRUSTED_ORIGINS")

# --- Приложения -----------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    # DRF подключён заранее; эндпоинты появятся на этапе Э7.
    "rest_framework",
]

# Разбивка приложений по модели данных (docs/architecture/django-apps.md)
LOCAL_APPS = [
    "apps.core",
    "apps.accounts",
    "apps.customers",
    "apps.catalog",
    "apps.orders",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Общие шаблоны проекта: templates/base.html и папки по приложениям
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# --- База данных ----------------------------------------------------------
# Разработка: SQLite. Боевая СУБД: PostgreSQL 14+ (см. ER-схему, задание 3).
# Переключение — только значением DATABASE_URL, код менять не нужно.

DATABASES = {
    "default": dj_database_url.parse(
        env("DATABASE_URL", f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
        conn_max_age=600,
    )
}

# Относительный путь к файлу SQLite считаем от папки django/, а не от места запуска
_default_db = DATABASES["default"]
if (
    _default_db["ENGINE"].endswith("sqlite3")
    and _default_db["NAME"] != ":memory:"
    and not os.path.isabs(str(_default_db["NAME"]))
):
    _default_db["NAME"] = str(BASE_DIR / _default_db["NAME"])

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Пароли ---------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Язык и время ---------------------------------------------------------

LANGUAGE_CODE = env("LANGUAGE_CODE", "ru")
TIME_ZONE = env("TIME_ZONE", "Europe/Moscow")
USE_I18N = True
USE_TZ = True  # в БД хранится UTC (как в API-контракте), на экране — местное время

# --- Статика и медиа ------------------------------------------------------

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # исходники: css/, js/, img/
STATIC_ROOT = BASE_DIR / "staticfiles"    # сюда собирает collectstatic (не коммитится)

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"           # загруженные файлы (не коммитится)

# --- Django REST Framework (каркас; настройка — на этапе Э7) ---------------

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}
