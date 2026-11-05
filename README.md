# Django Backend Template

Reusable backend template based on Django REST Framework.

## Stack

- Python 3.12
- Django 5.2 LTS
- Django REST Framework
- PostgreSQL
- Docker

## Local development

### 1. Create virtual environment

python -m venv .venv

### 2. Activate environment

source .venv/Scripts/activate

### 3. Install dependencies

pip install -r requirements/development.txt

### 4. Configure environment

cp .env.example .env

### 5. Start services

docker compose up --build -d

### 6. Run tests

docker compose exec web pytest

## API

- Health: /api/health/
- Swagger: /api/docs/
- Admin: /admin/