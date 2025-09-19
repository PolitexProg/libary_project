# Django DRF Project

## Описание
REST API для управления книгами с авторизацией и документацией Swagger.

## Быстрый старт

1. Клонируйте репозиторий и перейдите в папку проекта:
   ```sh
   git clone <repo_url>
   cd myproject-drf
   ```
2. Создайте и активируйте виртуальное окружение:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
4. Примените миграции:
   ```sh
   python manage.py migrate
   ```
5. Запустите сервер:
   ```sh
   python manage.py runserver
   ```
6. Документация API:
   - Swagger: http://localhost:8000/swagger/
   - Redoc: http://localhost:8000/redoc/

## Тесты
Добавьте тесты в `app/tests.py` и запустите:
```sh
python manage.py test
```

## Лицензия
MIT
