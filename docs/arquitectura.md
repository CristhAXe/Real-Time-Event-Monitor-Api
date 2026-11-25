# Arquitectura

## Estado actual

```
Cliente HTTP ──► FastAPI (main.py) ──► lista en memoria `events`
```

- `GET /health`: comprobación de vida, devuelve `{"status": "ok"}`.
- `GET /events`: devuelve todos los eventos.
- `POST /events`: valida el cuerpo con `EventCreate` (`type`, `message`, `severity`) y lo guarda con un `id` incremental.

No hay persistencia: Postgres y Redis se levantan con Docker Compose, pero la app todavía no los usa.

## Dirección prevista

Según las dependencias declaradas (aún sin implementar):

```
Cliente ──► FastAPI ──► Postgres (SQLAlchemy async + Alembic)
                │
                ├──► Redis (pub/sub o caché de eventos)
                └──► WebSocket ──► clientes suscritos en tiempo real
```

- Configuración por variables de entorno con `pydantic-settings`.
- `google-generativeai` para análisis de eventos con Gemini (sin definir).

Actualiza este documento cuando una pieza pase de "prevista" a implementada.
