BASE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PYENV_FILE := $(BASE_DIR).python-version
VENV ?= $(BASE_DIR)venv/

help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

test: $(VENV)bin/pytest ## Run tests.
	cd $(BASE_DIR) && \
	. $(VENV)bin/activate && \
	pytest

clean_test: ## Delete the unnecessary resources for test target.
	rm -rf $(BASE_DIR).pytest_cache

$(VENV)bin/pytest: $(VENV)bin/activate
	cd $(BASE_DIR) && \
	. $(VENV)bin/activate && \
	pip install --upgrade pip && \
	pip install -e .[test]

$(PYENV_FILE):
	cd $(BASE_DIR) && \
	pyenv local {{ cookiecutter.python_version }}

$(VENV)bin/activate: $(PYENV_FILE)
	cd $(BASE_DIR) && python -m venv $(VENV)

.PHONY: help
