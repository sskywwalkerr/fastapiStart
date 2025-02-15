# Стек:
* Python >= 3.12
* FastAPI >= 0.115.2
* fastapi-cache2 0.2.1
* Асинхронность
* Anyio
* JWT
* Alembic
* SQLAlchemy 2.0.4
* Docker
* PostgreSQL
* Asyncpg
* CORS
* Redis 4.5.2
* Celery 5.2.7
* Flower
* Uvicorn
* Gunicorn
* Prometheus
* Grafana


### Запуск через докер

* docker-compose up --build  
#### 1) Создать образ

    docker-compose build

#### 2) Запустить контейнер

    docker-compose up

#### 3) Перейти по адресу

    http://127.0.0.1:8000/docs

#### 4) Создать миграции 

    docker exec -it ApiFast-back poetry run alembic upgrade head

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

### 9) uvicorn api.db.main:app --reload
### 10) alembic upgrade head   
### 11) docker compose up -d & docker compose down -v      
### 12) celery -A api.celery_tasks.c_app worker --loglevel=INFO
### 13) pip install -r requirements.txt