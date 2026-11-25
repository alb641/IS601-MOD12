# IS601 Module 12 — FastAPI Calculator with JWT Authentication and Calculation BREAD

## Project Overview

Module 12 extends the FastAPI Calculator application by integrating JWT-based user authentication with PostgreSQL-backed calculation management. Users can register, log in, and perform Browse, Read, Edit, Add, and Delete (BREAD) operations on their calculations.

The application uses SQLAlchemy for database persistence, Pydantic for data validation, and FastAPI dependencies to protect calculation endpoints. Each calculation is associated with a user, ensuring authenticated users can access and manage only their own records.

## Technologies Used

- Python 3.13 and FastAPI
- PostgreSQL and SQLAlchemy
- Pydantic
- JWT authentication and HTTP Bearer security
- Docker and Docker Compose
- pytest
- GitHub Actions CI/CD
- Trivy security scanning

## Application Features

### User Authentication

Users can register through `/users/register` and log in through `/users/login`. Successful authentication returns a JWT access token.

Protected endpoints require a valid Bearer token. The application verifies the token, retrieves the associated user from PostgreSQL, and checks that the account is active.

### Calculation BREAD Operations

Operation --> HTTP Method --> Endpoint 
Add | POST | `/calculations` |
Browse | GET | `/calculations` |
Read | GET | `/calculations/{calc_id}` |
Edit | PUT | `/calculations/{calc_id}` |
Delete | DELETE | `/calculations/{calc_id}` |

### User-Specific Data Access

Each calculation contains a `user_id` that identifies its owner. Browse, Read, Edit, and Delete queries filter records using the authenticated user's ID.

Requests for nonexistent calculations or calculations that do not belong to the authenticated user return a 404 response.

### PostgreSQL Persistence

SQLAlchemy models represent users and calculations, while PostgreSQL stores account information, calculation operands, operation types, and results.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/alb641/IS601-MOD12.git
cd IS601-MOD12
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Configure `DATABASE_URL`, `TEST_DATABASE_URL`, and `SECRET_KEY` as appropriate for the local environment. Keep secrets out of version control.

### 5. Start PostgreSQL

```powershell
docker compose up -d db
```

### 6. Start FastAPI

```powershell
python -m uvicorn main:app --reload
```

**Application:** http://127.0.0.1:8000  
**Swagger API Documentation:** http://127.0.0.1:8000/docs

## Using the API

1. Register an account using `POST /users/register`.
2. Log in using `POST /users/login`.
3. Copy the returned JWT access token.
4. Click Authorize in Swagger and enter the token.
5. Create, browse, read, update, or delete calculations.

Example calculation request:

```json
{
  "a": 10,
  "b": 5,
  "type": "Add"
}
```

The calculated result is `15`.

## Automated Testing

The project includes automated tests covering application functionality, database persistence, authentication, and calculation behavior.

Run the complete test suite:

```powershell
python -m pytest -q
```

**Latest confirmed local result: 94 passed, 1 skipped, 0 failed.**

## Docker and CI/CD

Docker provides a consistent containerized application environment. Docker Compose supports the PostgreSQL database service.

GitHub Actions automates testing, Docker image building, Trivy security scanning, and Docker Hub publishing.

## Repository

**GitHub:** https://github.com/alb641/IS601-MOD12  
