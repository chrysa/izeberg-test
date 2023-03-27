#!make
ifneq (,)
	$(error This Makefile requires GNU Make)
endif

__docker_compose_service=poke-izeberg
__docker_image=${__docker_compose_service}:0.0.1

__project_directory=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))

__remote_folder=projects/$(shell basename $(CURDIR))

SHELL := /bin/bash

.DEFAULT_GOAL := help

.PHONY: $(shell grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | cut -d":" -f1 | tr "\n" " ")

help: ## This help dialog => help
	@echo "Hello to the Makefile\n"
	@IFS=$$'\n'
	@printf "%-40s %-100s %-60s\n" "target" "help" "usage"
	@printf "%-40s %-100s %-60s\n" "------" "----" "----"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | sed 's/:.*##/##/g' | tr ':' ' ' | tr '=>' '##'| awk 'BEGIN {FS = "##"}; {printf "\033[36m%-40s\033[0m %-100s %-60s\n", $$1, $$2, $$3}'

build: ## build container => build
	@docker compose build ${__docker_compose_service}

connect-dev: ## connect on dev container => connect-dev
	@docker compose run -it --rm ${__docker_compose_service}-dev sh

dev: migrate ## run application on dev configuration without mounted sources => dev
	@docker compose up ${__docker_compose_service}-dev

migrate: ## migrate models to database => migrate
	@docker compose run -it --rm --volume ${PWD}/src/:/poke-izeberg-app --entrypoint "manage.py makemigrations --verbosity 3" ${__docker_compose_service}-dev
	@docker compose run -it --rm --volume ${PWD}/src/:/poke-izeberg-app --entrypoint "manage.py migrate --verbosity 3" ${__docker_compose_service}-dev

outdated: ## outdated python packages => outdated
	@docker compose run -it --rm ${__docker_compose_service} pip list --outdated

pre-commit: ## run pre-commit => pre-commit
	@pre-commit validate-config
	@pre-commit validate-manifest
	@pre-commit install-hooks
	@pre-commit autoupdate --bleeding-edge
	@pre-commit run --all-files --hook-stage manual --verbose

prune: ## remove all stuff associated to project on docker => prune
	@docker compose down --rmi all --volumes
	@docker compose rm -f

up: ## run services with logs following => up
	@docker compose up ${__docker_compose_service}

up-detach: ## run services without logs following => up-detach
	@docker compose up --detach ${__docker_compose_service}
