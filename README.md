## Технологический стек

| Компонент          | Версия       | Описание                          |
|--------------------|--------------|-----------------------------------|
| **Python**         | 3.12+        | Язык программирования             |
| **FastAPI**        | 0.115.2      | Веб-фреймворк                     |
| **PostgreSQL**     | 15.3         | Основная БД                       |
| **Redis**          | 4.5.2        | Кэширование и брокер сообщений    |
| **SQLAlchemy**     | 2.0.4        | ORM для работы с БД               |
| **Alembic**        | 1.13.1       | Миграции БД                       |
| **Celery**         | 5.2.7        | Асинхронные задачи                |
| **Docker**         | 24.0.6       | Контейнеризация                   |



## Быстрый старт

### Запуск через Docker

#### 1) Создать образ

    docker-compose build  

#### 2) Запустить контейнер

    docker-compose up -d 

#### 3) Документация API

    http://127.0.0.1:8000/docs

#### 4) Создать и применить миграции

    docker exec -it ApiFast-back poetry run alembic upgrade head
    docker exec -it ApiFast-back poetry run alembic revision --autogenerate -m "add_user_table"

#### 5) Создать суперюзера

    docker exec -it ApiFast-back python scripts/createsuperuser.py

#### 6) Если не выполняет команды 

    -Войти в контейнер - docker exec -it ApiFast-back bash
    -Выполнить команды без docker exec -it ApiFast-back

#### 7) Если нужно очистить бд 

    docker-compose down -v

### 8) Локальные команды

    alembic init migrations
    alembic revision --autogenerate -m "comment"
    alembic upgrade heads
    make up/down


* Полезные команды
### 9) uvicorn api.db.main:app --reload
### 10) alembic upgrade head   
### 11) docker compose up -d & docker compose down -v      
### 12) celery -A api.celery_tasks.c_app worker --loglevel=INFO
### 13) pip install -r requirements.txt# vulnerability_monitor
