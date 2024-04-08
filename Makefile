.PHONY: stop logs restart up debug build

DOCKER_DEVICES_APP=devices_app

build-dev:
	sort -u -t '=' -k 1,1 .env.development .env.common > .env
	docker compose -f docker-compose.yaml build

up:
	docker compose -f docker-compose.yaml up -d

stop:
	docker compose -f docker-compose.yaml stop

logs:
	docker logs $(DOCKER_DEVICES_APP) -f --tail 50

restart:
	docker compose -f docker-compose.yaml restart

debug:
	docker attach $(DOCKER_DEVICES_APP)

test:
	docker exec -it $(DOCKER_DEVICES_APP) python3 -m pytest -s -v $(args)

install-pre-commit-hooks:
	poetry run pre-commit install
	poetry run pre-commit install --install-hooks --hook-type commit-msg