# Настройка репозитория на GitHub (для ТЛ)

## 1. Создать репозиторий

1. github.com → **+** → **New repository**.
2. Имя: `rkis-project`. Видимость — как требует преподаватель (Private/Public).
3. **Не** ставьте галочки «Add a README», «.gitignore», «license»: все файлы уже подготовлены.
4. **Create repository**.

## 2. Загрузить подготовленные файлы (первый коммит в `main`)

Через сайт: на странице пустого репозитория нажмите **uploading an existing file**, перетащите всё содержимое папки `rkis-project` (включая `.github`, `.gitignore`, `README.md`), в поле сообщения введите:

```
chore: add repository structure, docs and project skeletons
```

и нажмите **Commit changes**.

Через терминал (если установлен Git), из папки `rkis-project`:

```
git init -b main
git add .
git commit -m "chore: add repository structure, docs and project skeletons"
git remote add origin https://github.com/<ваш-логин>/rkis-project.git
git push -u origin main
```

Проверьте, что файл `.env` и папки `venv/`, `node_modules/` в репозиторий **не попали**.

## 3. Добавить команду

**Settings → Collaborators → Add people**: Криницын В., Шукуров С., Баранов А., Васильева С. (по логину или почте GitHub). Участники принимают приглашение по письму.

## 4. Защитить ветку `main`

**Settings → Branches → Add branch ruleset** (или Add rule), ветка `main`:

- Require a pull request before merging;
- Required approvals: 1.

На бесплатном аккаунте для приватных репозиториев защита веток может быть недоступна. Тогда правило действует по договорённости, и это записывается в протокол встречи.

## 5. Завести рабочие ветки

Каждый создаёт ветку под свою задачу от `main` (на сайте: выпадающий список веток → ввести имя → **Create branch**). Имена для первых задач:

| Кто | Ветка |
|---|---|
| ТЛ | `feature/repo-structure` |
| БР | `feature/django-skeleton` |
| ФР | `feature/frontend-base-layout` |
| ДР | `feature/desktop-skeleton` |
| МР | `feature/mobile-skeleton` |
| ДИ | `feature/design-system` |
| QA | `feature/qa-launch-checklist` |

Работа в ветке → Pull Request в `main` → ревью → merge → удаление ветки. Подробности — `docs/git-workflow.md`.

## 6. Проверка у других участников

Проверку запуска (чек-лист `tests/checklists/01-launch-checklist.md`) выполняют минимум на двух машинах: у QA и у кого-то ещё из команды. Шаги, которые потребовались сверх README, записываются в протокол и в баг-репорты.
