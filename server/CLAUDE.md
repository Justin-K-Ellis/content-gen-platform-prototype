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

## Architecture

This is an early-stage FastAPI prototype. The entry point is `app/main.py`, which creates the `FastAPI` app instance and registers routes directly. There is no project-level `pyproject.toml` — dependencies are managed with `requirements.txt` and a `.venv` virtual environment (Python 3.14).

The `app/` package is the sole application module. As the project grows, routes, models, and services should be organized as sub-modules within `app/`.
