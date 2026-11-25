# Decisiones

## 2026-08-05 · uv como gestor de dependencias
- **Contexto**: las dependencias estaban en `requirements.txt` sin lockfile.
- **Decisión**: `pyproject.toml` + `uv.lock` con versiones fijadas; entorno en `.venv/`.
- **Alternativas descartadas**: pip + `requirements.txt` (sin lock reproducible ni gestión de Python).

## 2026-08-01 · Postgres y Redis con Docker Compose
- **Contexto**: hacen falta base de datos y caché/mensajería en local.
- **Decisión**: `compose.yaml` con `postgres:18` y `redis`, credenciales leídas de `.env`.
- **Alternativas descartadas**: instalarlos en el sistema (difícil de reproducir entre máquinas).

## 2026-11-25 · Limpieza del repo y contexto para agentes
- **Contexto**: había un venv de WSL en la raíz (`bin/`, `lib/`, `pyvenv.cfg`), `.pyc` versionados, `.env -example` vacío y Redis con `--requirepass` sin valor.
- **Decisión**: un único `.venv/` de uv, `.gitignore` ampliado, `.env.example` con las variables y compose leyendo contraseñas de `.env` (falla si faltan). Volumen de Postgres 18 en `/var/lib/postgresql`.
- **Alternativas descartadas**: contraseñas fijas en `compose.yaml` (secretos en git).
