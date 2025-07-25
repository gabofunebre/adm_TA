# Movimientos de Dinero

Backend en FastAPI para registrar movimientos entre cuentas.

## Requisitos
- Docker y docker-compose

## Desarrollo


1. Copia `.env.example` a `.env` y ajusta los valores de la base de datos, `DB_PATH` y JWT.

2. Ejecuta:
   ```
   docker-compose up --build -d
   ```

3. La aplicación se une a dos redes: `movdin_net` para comunicarse con la base y `nginx_net` para tu proxy.

4. Configura `DB_PATH` en el archivo `.env` para elegir la ruta donde se guardará
   el volumen de PostgreSQL.

