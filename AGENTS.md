# Real-Time Event Monitor API

API para registrar y consultar eventos (tipo, mensaje, severidad) en tiempo real.

## Stack
- Python >=3.12 (desarrollo con 3.14, ver `.python-version`) gestionado con uv
- FastAPI + Uvicorn, Pydantic v2
- Previsto (en dependencias, aún sin usar): SQLAlchemy async + asyncpg, Alembic, Redis, websockets, pydantic-settings, google-generativeai
- Infra local: Docker Compose (Postgres 18, Redis)

## Comandos
- Instalar: `uv sync`
- Servicios: `docker compose up -d` (requiere `.env`, copia de `.env.example`)
- Dev: `uv run uvicorn real_time_event_monitor_api.main:app --reload`
- Test: sin tests todavía
- Lint/typecheck: sin configurar

## Mapa
- `src/real_time_event_monitor_api/main.py`: app FastAPI, modelo `EventCreate` y endpoints
- `compose.yaml`: Postgres y Redis de desarrollo
- `.env.example`: variables necesarias (sin valores reales)

## Reglas del proyecto
- Dependencias con versión fijada en `pyproject.toml`; gestiona con `uv add`/`uv sync`, nunca pip. Commitea `uv.lock`.
- El único entorno virtual es `.venv/` (lo crea uv). No crees venvs en la raíz.
- Los eventos viven en memoria (lista en `main.py`): se pierden al reiniciar y el `id` es `len + 1`.
- Postgres 18 monta el volumen en `/var/lib/postgresql` (no en `/data`).

## Pull requests
- Rama desde `main` actualizado con prefijo de tipo: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/` + descripción corta (`feat/websocket-eventos`).
- Título en Conventional Commits; descripción con la plantilla `.github/pull_request_template.md` (qué, por qué, cómo probarlo, riesgos).
- PR pequeño: un objetivo y < ~400 líneas. Si crece, divídelo en PRs encadenados.
- Abre como draft si no está listo; pide revisión solo con el checklist completo.
- Al menos una aprobación antes del merge; nunca push directo a `main`.
- Comentarios de revisión: se resuelven con commits nuevos (no force-push durante la revisión) y quien revisa marca como resuelto.
- Merge con squash; borra la rama tras el merge.

## Contexto
- Arquitectura: `docs/arquitectura.md`
- Decisiones: `docs/decisiones.md` (añade una entrada al tomar una decisión relevante)
