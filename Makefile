.PHONY: help install lint tests build clean

help:
	@echo "'make install':  Installs dependencies and pre-commit hooks"
	@echo "'make lint':     Runs ruff and ty via pre-commit on all files"
	@echo "'make tests':    Runs the test suite"
	@echo "'make build':    Builds a Python sdist and wheel"
	@echo "'make clean':    Removes build artifacts"

install:
	uv sync --extra dev
	uv run pre-commit install

lint:
	uv run pre-commit run --all-files

tests:
	uv run pytest

build:
	uv build

clean:
	rm -rf dist/
