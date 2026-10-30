# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the server

```bash
python -m app.main
```

Uvicorn is invoked directly in `app/main.py` with hot reload enabled on port 8000.

## Running tests

```bash
python -m pytest test/ -v
```

## Architecture

FastAPI prototype using a controller-service-repository pattern. Entry point is `app/main.py`, which creates the `FastAPI` app instance and registers routers via `app/router.py`. No `pyproject.toml` — dependencies managed with `requirements.txt` and a `.venv` virtual environment (Python 3.14).

### Layer responsibilities

- **Controllers** (`app/controllers/`): HTTP concerns only — route definitions, request/response models, status codes. Receive injected services via `Depends`.
- **Services** (`app/services/`): business logic and `Cat` → `CatPublic` projection. Receive an injected repository.
- **Repositories** (`app/repositories/`): database queries via SQLModel. Own `session.commit()`. Return domain models (`Cat`), not response models.

### Dependency injection

`app/utils/dependencies.py` holds the `Depends` provider chain and `Annotated` type aliases (e.g. `CatServiceDep`). This is the only place that wires the layers together. Controllers import these aliases; they do not instantiate services or repositories directly.

### Repository interfaces

Each repository module defines a `Protocol` (e.g. `CatRepositoryProtocol`) alongside the concrete class. Services are typed against the protocol, enabling fake implementations in unit tests without subclassing.

### Database

SQLite (`gtec.db`) via SQLModel/SQLAlchemy. Models live in `db/models/`. Engine and `get_session` are in `db/engine.py`. `db/models/__init__.py` registers all models so `SQLModel.metadata.create_all` picks them up.

### Testing

- `test/conftest.py` — shared `session` (in-memory SQLite, fresh per test) and `client` (TestClient with `get_session` overridden) fixtures.
- `test/end_to_end/` — full HTTP tests through `TestClient`. Never touch `gtec.db`.
- `test/unit/` — unit tests using fake repository implementations. No database, no FastAPI.
