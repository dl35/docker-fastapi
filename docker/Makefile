all: help

%:
	@:

help:
	@echo "usage:"
	@echo
	@echo "  make build"
	@echo "  make down"
	@echo "  make up"
	


CC=docker-compose


up: down
	$(CC) up

build: down
	
	$(CC) build --force-rm  --no-cache

down:
	$(CC) down  --remove-orphans --rmi local

dev:
	
	$(CC) run --service-ports fastapi bash