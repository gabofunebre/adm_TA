# Helper Makefile for development

CONTAINER ?= app_mov-dinero
DB_CONTAINER ?= db_mov-dinero

# Run a command inside the main container
run:
	docker exec -it $(CONTAINER) $(filter-out $@,$(MAKECMDGOALS))

# Basic commands
up:
	docker compose up --build -d

down:
	docker compose down

down-v:
	docker compose down -v

logs:
	docker compose logs -f || true

logs-db:
	docker logs -f $(DB_CONTAINER) || true

shell:
	docker exec -it $(CONTAINER) /bin/bash

prune:
	docker system prune

rebuild:
	make down
	make up

start:
	docker start $(CONTAINER)

stop:
	docker stop $(CONTAINER)

restart:
	docker restart $(CONTAINER)

ps:
	docker ps

push:
	git add .
	git commit -m "$(word 2, $(MAKECMDGOALS))"
	git push

pull:
	git pull origin main

# Allow targets with arguments at the end
%:
	@:
