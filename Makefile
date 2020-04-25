#
# Makefile for easier installation and cleanup.
#
# Uses self-documenting macros from here:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables --no-builtin-rules

PACKAGE=ffcount
DOC_DIR='./docs/'

.PHONY: help cover

.DEFAULT_GOAL := help

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
		 awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m\
		 %s\n", $$1, $$2}'

release: ## Make a release
	python make_release.py

in: inplace
inplace:
	python setup.py build_ext -i

install: ## Install for the current user using the default python command
	python setup.py build_ext --inplace
	python setup.py install --user

test: develop ## Run nosetests using the default nosetests command
	python -m unittest discover -v -f -s ./tests

clean: ## Clean build dist and egg directories left after install
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./$(PACKAGE).egg-info
	rm -f MANIFEST
	find . -type f -iname '*.pyc' -delete
	find . -type d -name '__pycache__' -empty -delete

develop: ## Install a development version of the package needed for testing
	python setup.py develop --user

dist: ## Make Python source distribution
	python setup.py sdist
