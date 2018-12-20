TEST_PATH=./tests
PROJECT_NAME=generator_domain

.PHONY: test clean-pyc develop codestyle install

test: clean-pyc 
	@( \
		source $(WORKON)/$(PROJECT_NAME)/bin/activate; \
		py.test --cov-report term-missing --cov-config setup.cfg --cov . --disable-pytest-warnings; \
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
		python -m flake8 || true; \
	)

install:
	@pip install --user -r requirements.txt;

run:
	@(\
		source $(WORKON)/$(PROJECT_NAME)/bin/activate; \
		python run.py; \
	)

local:
	@(\
		docker build -t generator_domain; \
		docker run -d -p 4000:8000 generator_domain; \
	)
	
ci-unit: test codestyle