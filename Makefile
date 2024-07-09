.DEFAULT_GOAL := help

SCRAPER_CMD = cd scraper && make

.PHONY: help start run build destroy

help:
	@echo "Usage:"
	@echo "  make start     - Build and load docker image, run TelSök and Scraper backend"
	@echo "  make destroy   - Stop and destroy containers"
	@echo "  make build     - Only build and load docker image."
	@echo "  make run       - Only run TelSök and Scraper backend."

start: build run

build:
	nix build .\#dockerImage
	docker load < result

run:
	docker run --rm -d -t \
        --network host \
        --name telsok \
        --env-file .env \
        telsok:latest

	$(SCRAPER_CMD) up

destroy:
	docker stop telsok || true && docker rm telsok || true
	$(SCRAPER_CMD) down
