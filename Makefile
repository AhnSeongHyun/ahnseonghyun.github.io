# Makefile for ash84.io static site

.PHONY: build clean format dev install

# Install zv package in development mode
install:
	pip install -e .

# Build the static site
build: install
	zv build

# Clean generated files
clean: install
	zv clean

dev: 
	zv build
	python -m http.server 8000  --directory ./docs 

format: 
	ruff format .