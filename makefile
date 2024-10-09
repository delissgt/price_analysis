# Wraps common operations for project

# Set more sensible defaults
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

# Target configs
.DEFAULT_GOAL := help

DOCKER_COMPOSE = docker-compose -f dev.yml

# Objetives
.PHONY: up down logs build rebuild

build: ## Builds docker image
> @docker build -t price_analysis_img:dev .

down: ## Stop container
> $(DOCKER_COMPOSE) down

help:  ## Displays help.
> @grep -E '^[a-zA-Z_-]+[0-9]*:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

logs: ## View container logs
> $(DOCKER_COMPOSE) logs -f

rebuild: ## Rebuild container
> $(DOCKER_COMPOSE) up --build

up: ## Start container
> $(DOCKER_COMPOSE) up




