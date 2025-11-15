.PHONY: help setup up down build restart logs migrate makemigrations createsuperuser shell test clean

help:
	@echo "The Circus Grove - Available Commands:"
	@echo ""
	@echo "  make setup          - Initial setup (create .env, start containers, run migrations)"
	@echo "  make up             - Start all containers"
	@echo "  make down           - Stop all containers"
	@echo "  make build          - Build Docker images"
	@echo "  make restart        - Restart all containers"
	@echo "  make logs           - View logs from all containers"
	@echo "  make migrate        - Run database migrations"
	@echo "  make makemigrations - Create new migrations"
	@echo "  make createsuperuser - Create Django superuser"
	@echo "  make shell          - Open Django shell"
	@echo "  make test           - Run tests"
	@echo "  make clean          - Stop containers and remove volumes"

setup:
	@./setup.sh

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

restart:
	docker compose restart

logs:
	docker compose logs -f

migrate:
	docker compose exec backend python manage.py migrate

makemigrations:
	docker compose exec backend python manage.py makemigrations

createsuperuser:
	docker compose exec backend python manage.py createsuperuser

shell:
	docker compose exec backend python manage.py shell

test:
	docker compose exec backend python manage.py test

clean:
	docker compose down -v
