PYTHON = python3.13

.PHONY = help install lint tests build docs clean

help:
	@echo "'make install': Setups up a virtualenv and installs pyproject deps using uv"
	@echo "'make lint: Runs the linters defined in .pre-commit-config.yaml"
	@echo "'make tests': Runs unit tests with pytest"
	@echo "'make build': Builds a Python sdist and wheel"
	@echo "'make docs': Builds a Python sphinx docs"
	@echo "'make clean': Removes development files and virtualenv"


install:
	uv sync --extra dev
	uv run pre-commit install
lint:
	uv run pre-commit run --all-files
tests:
	uv run pytest test/
	uv run --env-file envs/.env.numbajit pytest test/
build:
	uv build
docs:
	cd sphinx
	make html
	cd ..
clean:
	rm -rf .venv
