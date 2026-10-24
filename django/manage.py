#!/usr/bin/env python
"""Точка входа Django для административных команд."""
import os
import sys


def main():
    # По умолчанию — настройки для разработки. Боевые настройки выбираются
    # переменной окружения DJANGO_SETTINGS_MODULE=config.settings.prod.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Активировано ли виртуальное "
            "окружение и установлены ли зависимости "
            "(pip install -r requirements.txt)?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
