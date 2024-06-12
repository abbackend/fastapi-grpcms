init: build up
restart: down up

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans