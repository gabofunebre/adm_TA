# adm_TA

Backend en FastAPI que provee registro de usuarios y login.

## Requisitos
- Docker y docker-compose

## Desarrollo

1. Copia `.env.example` a `.env` y ajusta los valores de la base de datos, `DB_PATH` y JWT.

2. Ejecuta:
   ```
   docker-compose up --build -d
   ```

3. Los servicios `db_TA` y `adm_TA` se comunican a través de la red `net_TA`.
