# Real-Time Event Monitor API

API REST con FastAPI para registrar y consultar eventos (tipo, mensaje y severidad).

> Estado: fase inicial. Los eventos se guardan en memoria y se pierden al reiniciar. La persistencia en Postgres, Redis y el envío por WebSocket están previstos.

## Características

- Alta de eventos con validación automática del cuerpo.
- Listado de todos los eventos registrados.
- Endpoint de salud para comprobar que el servicio está vivo.
- Documentación interactiva de la API (Swagger) incluida.

## Requisitos

- Python ≥ 3.12
- [uv](https://docs.astral.sh/uv/)
- Docker con Docker Compose (para Postgres y Redis)

## Instalación

```bash
uv sync
```

## Configuración

Copia `.env.example` a `.env` y rellena:

| Variable | Obligatoria | Descripción |
|---|---|---|
| `POSTGRES_PASSWORD` | Sí | Contraseña de Postgres (`<POSTGRES_PASSWORD>`) |
| `POSTGRES_DB` | No | Nombre de la base de datos (por defecto `event_monitor`) |
| `REDIS_PASSWORD` | Sí | Contraseña de Redis (`<REDIS_PASSWORD>`) |

Levanta los servicios:

```bash
docker compose up -d
```

## Uso

```bash
uv run uvicorn real_time_event_monitor_api.main:app --reload
```

La API queda en `http://127.0.0.1:8000` y la documentación en `http://127.0.0.1:8000/docs`.

Ejemplo mínimo:

```bash
curl -X POST http://127.0.0.1:8000/events \
  -H "Content-Type: application/json" \
  -d '{"type": "login", "message": "Usuario conectado", "severity": "info"}'
```

Respuesta:

```json
{"id": 1, "type": "login", "message": "Usuario conectado", "severity": "info"}
```

## Endpoints

| Método | Ruta | Qué hace |
|---|---|---|
| `GET` | `/health` | Devuelve `{"status": "ok"}` |
| `GET` | `/events` | Lista los eventos |
| `POST` | `/events` | Crea un evento |

## Documentación

- Arquitectura: [docs/arquitectura.md](docs/arquitectura.md)
- Decisiones técnicas: [docs/decisiones.md](docs/decisiones.md)

## Contribuir

1. Crea una branch desde `main`.
2. Tests primero (deben fallar), luego la implementación.
3. Commits en Conventional Commits y PR con descripción (qué, por qué, cómo probarlo).
