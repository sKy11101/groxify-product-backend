# Groxify Product Backend

Django REST API starter for the existing Groxify React website.

## Stack
- Python
- Django
- Django REST Framework
- PostgreSQL (local development can use SQLite until PostgreSQL is configured)
- Planned production: AWS EC2 + Elastic IP + RDS PostgreSQL
- Planned product media: private Amazon S3 + CloudFront

## 1. Create environment and install dependencies

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

## 2. Configure environment

Copy `.env.example` to `.env` and update values.

For initial local testing, keep `DB_HOST=127.0.0.1` and configure PostgreSQL locally,
or temporarily use SQLite by setting `DB_ENGINE=sqlite` in `.env`.
The default settings use PostgreSQL when DB_NAME is configured.

## 3. Create database and run migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 4. API endpoints

- `GET /api/health/`
- `GET /api/categories/`
- `GET /api/products/`
- `GET /api/products/<id>/`

Write operations are restricted to authenticated staff users:
- `POST /api/categories/`
- `POST /api/products/`
- `PUT/PATCH/DELETE /api/products/<id>/`

Django Admin: `/admin/`

## Notes
- This is the initial backend scaffold. Do not point the live website to it until API,
  CORS, authentication, HTTPS, database backups, and production settings are tested.
- Product images currently use Django's local media storage for development.
  S3 + CloudFront integration will be added in a dedicated deployment step.
