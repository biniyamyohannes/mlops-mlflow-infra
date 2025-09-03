# Makefile for MLflow + postgres + S3 cleanup

# Export everything from .env (if it exists)
ifneq (,$(wildcard .env))
    include .env
    export $(shell sed -n 's/^\([^#=]\+\)=.*/\1/p' .env)
endif

.PHONY: help up down rebuild s3-clean clean

help:
	@echo "Targets:"
	@echo "  up        - build & start mlflow stack"
	@echo "  down      - stop & remove containers, images, volumes, orphans"
	@echo "  rebuild   - force rebuild & restart"
	@echo "  logs      - tail mlflow logs"
	@echo "  ps        - list project containers"
	@echo "  s3-clean  - empty S3 path from .env (MLFLOW_ARTIFACTS_DESTINATION or S3_ARTIFACT_ROOT)"
	@echo "  clean     - down + s3-clean"
	@echo "  nuke      - remove ALL Docker state (DANGEROUS)"

up:
	docker compose up -d --build

down:
	docker compose down --rmi all -v --remove-orphans

rebuild:
	docker compose build --no-cache
	docker compose up -d

s3-clean:
	@if [ -n "$$MLFLOW_ARTIFACTS_DESTINATION" ]; then \
		S3_PATH=$$MLFLOW_ARTIFACTS_DESTINATION; \
	elif [ -n "$$S3_ARTIFACT_ROOT" ]; then \
		S3_PATH=$$S3_ARTIFACT_ROOT; \
	else \
		echo "ERROR: set MLFLOW_ARTIFACTS_DESTINATION or S3_ARTIFACT_ROOT in .env"; exit 1; \
	fi; \
	echo "Emptying: $$S3_PATH"; \
	aws s3 rm "$$S3_PATH" --recursive --region "$$AWS_DEFAULT_REGION"

clean: down s3-clean
