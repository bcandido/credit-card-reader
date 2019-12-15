SHELL:=/bin/bash

PYTHON?=$(shell which python3)
PIP?=$(shell which pip)
VENV=$(CURDIR)/venv

image?=assets/credit_card_01.png

all: requirements run

requirements:
	source $(VENV)/bin/activate && \
	$(PIP) install -r requirements.txt --upgrade

run:
	source venv/bin/activate && \
	$(PYTHON) src/main.py --image $(image)

venv:
	$(PYTHON) -m venv $(VENV)