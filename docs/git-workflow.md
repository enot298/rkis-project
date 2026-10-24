# Git-конвенция

Утверждена на установочной встрече 02.10.2026 (документ «План проекта», раздел 5). Здесь — краткая версия для ежедневной работы.

## Ветки

Все ветки создаются от `main`. В `main` напрямую не коммитим, только через Pull Request.

| Тип | Формат | Пример |
|---|---|---|
| Новая функция | `feature/краткое-описание` | `feature/order-crud` |
| Исправление бага | `fix/краткое-описание` | `fix/login-validation` |
| Срочное исправление | `hotfix/краткое-описание` | `hotfix/api-500-error` |
| Документация | `docs/краткое-описание` | `docs/api-contract` |
| Релиз | `release/версия` | `release/v1.0` |
| Рефакторинг | `refactor/краткое-описание` | `refactor/models-cleanup` |

## Коммиты

Формат: `тип(область): краткое описание`. Язык — английский (решение встречи 02.10.2026).

Типы: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`.
Области: `backend`, `frontend`, `desktop`, `mobile`, `design`, `api`, `db`, `qa`, `docs`.

Примеры:

```
feat(backend): add Django project skeleton and settings
feat(frontend): add base.html and static structure
chore: update .gitignore
docs(qa): add launch checklist
```

## Слияние

1. В `main` — только через Pull Request.
2. PR ревьюит минимум один участник, не автор.
3. Перед слиянием ветка актуализируется относительно `main`; конфликты решает автор.
4. Описание PR: что сделано, зачем, как проверено (шаблон `.github/pull_request_template.md`).
5. После слияния ветка удаляется.

## Кто кого ревьюит (предложение для встречи по старту)

| Автор PR | Ревьюер |
|---|---|
| Криницын В. (БР, ФР) | Минженков К.; шаблоны и стили дополнительно сверяет Баранов А. с макетом |
| Шукуров С. (ДР, МР) | Криницын В. |
| Баранов А. (ДИ) | Минженков К. |
| Васильева С. (QA) | Минженков К. |
| Минженков К. (ТЛ) | Васильева С. |

## Порядок слияния первых PR

1. `feature/repo-structure` (ТЛ): структура, README, `.gitignore`, шаблоны.
2. `feature/django-skeleton` (БР): проект, настройки, `requirements.txt`, `.env.example`.
3. `feature/frontend-base-layout` (ФР): `base.html`, статика (после п. 2).
4. `feature/design-system` (ДИ), `feature/desktop-skeleton` и `feature/mobile-skeleton` (ДР, МР), `feature/qa-launch-checklist` (QA): в любом порядке, они независимы.
