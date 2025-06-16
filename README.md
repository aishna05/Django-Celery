# Django-Celery

## Features
- JWT Authentication
- Public & Protected APIs
- Celery + Redis
- Telegram Bot Integration

## Setup
```bash
git clone https://github.com/aishna05/Django-Celery.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Environment Variables
Create .env:

ini
Copy
Edit
SECRET_KEY=...

## Run Project
bash
Copy
Edit
python manage.py runserver
celery -A internship worker --loglevel=info

## API Endpoints
POST /api/login/

GET /api/public/

GET /api/protected/