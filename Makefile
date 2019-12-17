SHELL:=/bin/bash

PYTHON?=$(CURDIR)/venv/bin/python
PYTEST?=$(CURDIR)/venv/bin/pytest
PIP?=$(CURDIR)/venv/bin/pip
VENV=$(CURDIR)/venv

image?=assets/credit_card_01.png

all: requirements run

requirements:
	source $(VENV)/bin/activate && \
	$(PIP) install -r requirements.txt --upgrade

run:
	source venv/bin/activate && \
	$(PYTHON) src/main.py --image $(image)

.PHONY: test
test:
	source $(VENV)/bin/activate && \
	export PYTHONPATH=./src && \
	$(PYTEST) -v test/test_*.py

venv:
	python3 -m venv $(VENV)