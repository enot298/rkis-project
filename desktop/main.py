"""Точка входа десктоп-клиента (Tkinter) для бухгалтера.

Запуск из папки desktop:  python main.py
"""
import sys

if sys.version_info < (3, 11):
    sys.exit("Нужен Python 3.11 или новее. Сейчас: " + sys.version.split()[0])

from ui.main_window import MainWindow  # noqa: E402  (импорт после проверки версии)


def main() -> None:
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
