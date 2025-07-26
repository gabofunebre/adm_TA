# Helper Makefile para desarrollo y automatización

# -----------------------------
# Variables
# -----------------------------
CONTAINER ?= app_mov-dinero
DB_CONTAINER ?= db_mov-dinero

# -----------------------------
# Ayuda
# -----------------------------
help:
	@echo "Makefile - Comandos disponibles:"
	@echo ""
	@echo "Contenedores:"
	@echo "  make up              - Levanta los contenedores con build"
	@echo "  make down            - Detiene y elimina los contenedores"
	@echo "  make down-v          - Idem down, pero elimina también los volúmenes"
	@echo "  make restart         - Reinicia el contenedor principal"
	@echo "  make start           - Inicia el contenedor principal si está detenido"
	@echo "  make stop            - Detiene el contenedor principal"
	@echo "  make ps              - Lista contenedores activos"
	@echo ""
	@echo "Logs y shell:"
	@echo "  make logs            - Muestra logs de todos los contenedores"
	@echo "  make logs-db         - Muestra logs del contenedor de base de datos"
	@echo "  make shell           - Abre una shell bash en el contenedor principal"
	@echo ""
	@echo "Frontend (React):"
	@echo "  make build-frontend  - Compila el frontend con Vite"
	@echo "  make install-frontend - Ejecuta npm install + build"
	@echo ""
	@echo "Rebuild:"
	@echo "  make rebuild         - Baja y vuelve a levantar los contenedores"
	@echo "  make rebuild-v       - Idem rebuild, eliminando también volúmenes"
	@echo "  make rebuild-all     - Rebuild completo: contenedores + frontend"
	@echo "  make rebuild-all-v   - Idem rebuild-all, pero elimina también volúmenes"
	@echo ""
	@echo "Git:"
	@echo "  make push MSG='msg'  - Hace commit y push con mensaje"
	@echo "  make pull            - Hace pull desde main"
	@echo ""
	@echo "Utilidades:"
	@echo "  make prune           - Limpia recursos docker sin usar"
	@echo "  make run comando     - Ejecuta un comando dentro del contenedor principal"
	@echo ""

# -----------------------------
# Contenedores
# -----------------------------
up:
	docker compose up --build -d

down:
	docker compose down

down-v:
	docker compose down -v

start:
	docker start $(CONTAINER)

stop:
	docker stop $(CONTAINER)

restart:
	docker restart $(CONTAINER)

ps:
	docker ps

# -----------------------------
# Logs y shell
# -----------------------------
logs:
	docker compose logs -f || true

logs-db:
	docker logs -f $(DB_CONTAINER) || true

shell:
	docker exec -it $(CONTAINER) /bin/bash

# -----------------------------
# Frontend
# -----------------------------
build-frontend:
	cd frontend && npm run build

install-frontend:
	cd frontend && npm install && npm run build

# -----------------------------
# Rebuild
# -----------------------------
rebuild:
	make down
	make up

rebuild-v:
	make down-v
	make up

rebuild-all:
	make down
	make build-frontend
	make up

rebuild-all-v:
	make down-v
	make build-frontend
	make up

# -----------------------------
# Git
# -----------------------------
push:
	git add .
	git commit -m "$(word 2, $(MAKECMDGOALS))"
	git push
	
pull:
	git pull origin main

# -----------------------------
# Utilidades
# -----------------------------
prune:
	docker system prune

# -----------------------------
# Ejecutar comando dentro del contenedor
# -----------------------------
run:
	docker exec -it $(CONTAINER) $(filter-out $@,$(MAKECMDGOALS))

# -----------------------------
# Target wildcard (ignora targets no declarados)
# -----------------------------
%:
	@:
