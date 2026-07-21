# MatchPoint Backend

Backend REST API powering MatchPoint, a tennis court reservation platform.

The API is built with Django REST Framework and exposes endpoints used by both the web frontend and the mobile application.

## Features

Current features include:

- User authentication (JWT)
- User profiles
- Clubs
- Courts
- Reservations
- Court availability
- Club employees

Upcoming features:

- Club analytics
- Dynamic pricing recommendations
- Player rankings
- Match history
- Tournaments

---

## Tech Stack

- Python 3.13+
- Django
- Django REST Framework
- PostgreSQL
- drf-spectacular (OpenAPI)
- pytest

---

## Project structure

```
src/
  matchpoint/
    clubs/
    courts/
    reservations/
    profiles/
    users/

tests/
```

Each application is responsible for a single business domain.

Business logic is implemented inside service classes whenever possible.

---

## Running locally

### 1. Clone the repository

```bash
git clone https://github.com/Corentin-dupriez/matchpoint.git
cd matchpoint
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file.

Example:

```env
DEBUG=True

POSTGRES_DB=matchpoint
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

SECRET_KEY=replace-me
```

---

### 5. Start PostgreSQL

The project uses PostgreSQL through Docker.

```bash
docker compose up -d 
```

---

### 6. Run migrations

```bash
python manage.py migrate
```

---

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

---

### 8. Start the server

```bash
python manage.py runserver
```

API available at

```
http://localhost:8000/api/
```

Swagger documentation

```
http://localhost:8000/api/schema/swagger-ui/
```

OpenAPI schema

```
http://localhost:8000/api/schema/
```

---

## Running tests

Run all tests

```bash
pytest
```

Run with coverage

```bash
pytest --cov --cov-report=term-missing
```

---

## Formatting

Format the project

```bash
ruff format .
```

Lint

```bash
ruff check .
```

---

## API Authentication

Authentication uses JWT.

Obtain a token

```
POST /api/token/
```

Refresh

```
POST /api/token/refresh/
```

Include the token

```
Authorization: Bearer <access_token>
```

---

## Development Guidelines

- Business logic belongs in service classes.
- Keep views thin.
- Prefer TDD when adding new features.
- Document every endpoint with drf-spectacular.
- Write type hints whenever possible.

---

## Current Roadmap

### MVP

- Clubs
- Courts
- Reservations
- Availability
- Profiles

### Phase 2

- Club analytics
- Dashboards
- Revenue metrics
- Occupancy reports

### Phase 3

- Rankings
- Match history
- Tournaments
- Gamification
