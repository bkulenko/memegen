TEST_PATH=./tests
PROJECT_NAME=generator_domain

.PHONY: test clean-pyc develop codestyle install

test: clean-pyc 
	@( \
		source $(WORKON)/$(PROJECT_NAME)/bin/activate; \
		py.test --cov-report term-missing --cov-config .coveragerc --cov .; \
	)
	
clean-pyc:
	@find . -name '*.pyc' -delete
	@find . -name '*.pyo' -delete

develop:
	@( \
		virtualenv $(WORKON)/$(PROJECT_NAME); \
		source $(WORKON)/$(PROJECT_NAME)/bin/activate; \
		pip install -r requirements.txt; \
	)

codestyle: clean-pyc 
	@(\
		source $(WORKON)/$(PROJECT_NAME)/bin/activate; \
		python -m flake8; \
	)

install:
	@pip install -r requirements.txt;
	
ci-unit: test codestyle