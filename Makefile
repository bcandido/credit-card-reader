SHELL:=/bin/bash

image?=assets/credit_card_01.png

all: requirements run

requirements:
	source venv/bin/activate && \
	pip install -r requirements.txt --upgrade

run:
	source venv/bin/activate && \
	python main.py --image $(image)