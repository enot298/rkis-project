# Проект «Учёт заказов для малого бизнеса»

Программный комплекс для приёма, обработки и выполнения заказов малого бизнеса. Командный проект по дисциплине РКИС, команда Минженкова.

## Содержание

1. [Состав системы](#состав-системы)
2. [Стек и версии](#стек-и-версии)
3. [Структура репозитория](#структура-репозитория)
4. [Как запустить: веб (Django)](#как-запустить-веб-django)
5. [Как запустить: десктоп (Tkinter)](#как-запустить-десктоп-tkinter)
6. [Как запустить: мобайл (React Native)](#как-запустить-мобайл-react-native)
7. [Секреты и переменные окружения](#секреты-и-переменные-окружения)
8. [Работа с Git](#работа-с-git)
9. [Решение типовых проблем](#решение-типовых-проблем)
10. [Документация](#документация)
11. [Команда](#команда)
12. [История изменений](#история-изменений)

## Состав системы

| Часть | Для кого | Технологии |
|---|---|---|
| Веб-клиент | менеджер | Django-шаблоны, HTML, CSS, JS |
| Десктоп-клиент | бухгалтер | Python, Tkinter |
| Мобильный клиент | кладовщик | React Native (Expo) |
| REST API | все клиенты | Django REST Framework (этап Э7) |

## Стек и версии

| Компонент | Версия |
|---|---|
| Python | 3.11 или новее |
| Django | 5.2 LTS (`5.2.1`) |
| Django REST Framework | 3.16.0 |
| СУБД в разработке | SQLite |
| СУБД боевая | PostgreSQL 14+ |
| Node.js | 18 или новее |
| Expo SDK / React Native | 52 / 0.76 |
| Платформы мобайла | Android 8.0+ (minSdk 26), iOS 15+ |
| Платформы десктопа | Windows 10+, macOS 12+, Ubuntu 22.04 |
| Браузеры | Chrome 110+, Firefox 110+, Safari 16+ |

Точные версии Python-пакетов — в `django/requirements.txt` и `desktop/requirements.txt`, пакетов Node — в `mobile/package.json`.

## Структура репозитория

```
rkis-project/
├── django/     Бэкенд и веб-клиент (Django)
├── desktop/    Десктоп-клиент (Tkinter)
├── mobile/     Мобильный клиент (React Native, Expo)
├── design/     Макеты, дизайн-система, SVG-ассеты
├── docs/       Документация, протоколы, шаблоны
├── tests/      Чек-листы, тест-планы, баг-репорты
├── .github/    Шаблоны Pull Request и задач
├── .gitignore
└── README.md
```

Что куда класть — в [docs/repository-structure.md](docs/repository-structure.md).

## Как запустить: веб (Django)

Нужен Python 3.11+. Все команды — из корня репозитория.

1. Перейдите в папку проекта:
   ```
   cd django
   ```
2. Создайте виртуальное окружение:
   ```
   python -m venv venv
   ```
3. Активируйте его:
   - Windows: `venv\Scripts\activate`
   - macOS / Linux: `source venv/bin/activate`
4. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
5. Создайте файл настроек из шаблона (значения для разработки уже подходят):
   - Windows: `copy .env.example .env`
   - macOS / Linux: `cp .env.example .env`
6. Примените миграции:
   ```
   python manage.py migrate
   ```
7. Создайте суперпользователя (логин и пароль придумайте сами):
   ```
   python manage.py createsuperuser
   ```
8. Запустите сервер:
   ```
   python manage.py runserver
   ```
9. Откройте в браузере:
   - главная: http://127.0.0.1:8000/
   - заказы (каркас): http://127.0.0.1:8000/orders/
   - админка: http://127.0.0.1:8000/admin/ (войти под суперпользователем)

Команды `manage.py` запускаются из папки `django` (там, где лежит `manage.py`).

## Как запустить: десктоп (Tkinter)

Нужен Python 3.11+. Tkinter входит в Python (на Ubuntu: `sudo apt install python3-tk`).

1. Перейдите в папку:
   ```
   cd desktop
   ```
2. (Рекомендуется) создайте и активируйте окружение, как в шагах 2–3 для веба.
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Запустите:
   ```
   python main.py
   ```

Откроется окно с меню, навигацией слева и разделами-заглушками. Подробнее — [desktop/README.md](desktop/README.md).

## Как запустить: мобайл (React Native)

Нужен Node.js 18+ и приложение Expo Go на телефоне (или эмулятор).

1. Перейдите в папку:
   ```
   cd mobile
   ```
2. Установите зависимости:
   ```
   npm install
   ```
3. Запустите:
   ```
   npx expo start
   ```
4. Отсканируйте QR-код в Expo Go или нажмите `a` (эмулятор Android) / `i` (симулятор iOS на macOS).

Если Expo Go сообщает о несовместимой версии SDK — см. [mobile/README.md](mobile/README.md). Там же объяснён выбор Expo.

## Секреты и переменные окружения

Секреты **не хранятся в коде и не коммитятся**. Настройки берутся из переменных окружения: локально — из файла `django/.env`, который игнорируется Git. Шаблон — `django/.env.example` (с комментарием к каждой переменной).

| Переменная | Назначение |
|---|---|
| `SECRET_KEY` | Секретный ключ Django (обязательна) |
| `DEBUG` | Режим отладки: `True` в разработке, `False` на сервере |
| `ALLOWED_HOSTS` | Разрешённые адреса сайта, через запятую |
| `DATABASE_URL` | Подключение к БД: `sqlite:///db.sqlite3` или `postgres://USER:PASSWORD@HOST:5432/DBNAME` |
| `CSRF_TRUSTED_ORIGINS` | Доверенные источники (только за HTTPS-прокси) |
| `TIME_ZONE`, `LANGUAGE_CODE` | Часовой пояс и язык (по умолчанию `Europe/Moscow`, `ru`) |

Для клиентов: адрес сервера десктопа — переменная `APP_API_BASE_URL`, мобайла — `EXPO_PUBLIC_API_BASE_URL`.

Боевой режим включается переменной `DJANGO_SETTINGS_MODULE=config.settings.prod`. В нём `DEBUG` выключен, а `SECRET_KEY` должен быть собственным.

## Работа с Git

- Ветки от `main`: `feature/*`, `fix/*`, `docs/*` и т. д.
- Коммиты на английском: `тип(область): описание`, например `feat(backend): add order model`.
- В `main` только через Pull Request с ревью одного участника (не автора).

Полные правила и таблица ревьюеров — [docs/git-workflow.md](docs/git-workflow.md).

## Решение типовых проблем

**`ModuleNotFoundError` (например, `No module named 'django'`).**
Не активировано виртуальное окружение или не установлены зависимости. Активируйте `venv` и выполните `pip install -r requirements.txt`.

**`Не задана переменная окружения SECRET_KEY`.**
Нет файла `.env`. Скопируйте `.env.example` в `.env` (шаг 5 запуска веба).

**`You have unapplied migration(s)`.**
Выполните `python manage.py migrate`.

**Порт 8000 занят.**
Запустите на другом порту: `python manage.py runserver 8001`.

**На странице нет стилей, в консоли браузера ошибки 404 для CSS.**
Убедитесь, что сервер запущен командой `runserver` из папки `django` при `DEBUG=True`.

**Команда `python` не найдена.**
На macOS/Linux используйте `python3`. На Windows установите Python с python.org и отметьте «Add Python to PATH».

**`No module named '_tkinter'` / `tkinter`.**
На Ubuntu: `sudo apt install python3-tk`. На Windows и macOS Tkinter ставится вместе с Python с python.org.

**`npm install` завершается ошибкой или Expo Go не открывает проект.**
Проверьте `node --version` (нужен 18+). Если версия SDK не совпадает с Expo Go: `npx expo install expo@latest`, затем `npx expo install --fix`.

**Телефон не подключается к Expo.**
Телефон и компьютер должны быть в одной Wi-Fi сети. Если не помогает: `npx expo start --tunnel`.

Не нашли свою ошибку — заведите баг-репорт по шаблону [docs/templates/bug-report.md](docs/templates/bug-report.md).

## Документация

| Документ | Где |
|---|---|
| Структура репозитория и правила размещения | [docs/repository-structure.md](docs/repository-structure.md) |
| Git-конвенция | [docs/git-workflow.md](docs/git-workflow.md) |
| Разбивка Django-приложений | [docs/architecture/django-apps.md](docs/architecture/django-apps.md) |
| Технические решения | [docs/architecture/decisions.md](docs/architecture/decisions.md) |
| Дизайн-система | [docs/design-system.md](docs/design-system.md) |
| Настройка GitHub (для ТЛ) | [docs/github-setup.md](docs/github-setup.md) |
| Протоколы встреч | [docs/protocols/](docs/protocols/) |
| Чек-лист запуска, баг-репорты | [tests/](tests/) |
| Макеты и ассеты | [design/README.md](design/README.md) |

## Команда

| Роль | Участник |
|---|---|
| ТЛ (тимлид) | Минженков К. |
| БР (бэкенд), ФР (фронтенд) | Криницын В. |
| ДР (десктоп), МР (мобайл) | Шукуров С. |
| ДИ (дизайн) | Баранов А. |
| QA (тестирование) | Васильева С. |

## История изменений

| Версия | Дата | Автор | Описание |
|---|---|---|---|
| 1.0 | 24.10.2026 | Минженков К. | Структура репозитория, каркасы всех частей, README, `.gitignore` (задание 4) |
