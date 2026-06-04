.PHONY: help install lint tests test-matrix build docs clean

help:
	@echo "'make install':      Creates hatch environments and installs pre-commit hooks"
	@echo "'make lint':         Runs ruff via pre-commit on all files"
	@echo "'make tests':        Runs unit tests in the default hatch environment"
	@echo "'make test-matrix':  Runs tests across Python 3.10, 3.11, 3.12, 3.13"
	@echo "'make build':        Builds a Python sdist and wheel"
	@echo "'make docs':         Builds Sphinx HTML docs"
	@echo "'make clean':        Removes hatch environments and build artifacts"

install:
	hatch env create
	hatch run pre-commit install

lint:
	hatch run pre-commit run --all-files

tests:
	hatch run test

test-matrix:
	hatch run test:run

build:
	hatch build

docs:
	cd sphinx && make html

clean:
	hatch env remove default
	hatch env remove test
	rm -rf dist/
