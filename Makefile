SHELL:=/bin/bash

PYTHON?=$(CURDIR)/venv/bin/python
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

test:
	source $(VENV)/bin/activate && \
	cd ./src/tests && \
	$(PYTHON) -m pytest

venv:
	python3 -m venv $(VENV)