TEST_PATH=./tests
PROJECT_NAME=generator_domain


test: clean-pyc
#	@$(foreach file,$(SOURCES), python -m pytest $(file);)
	@python -m pytest $(TEST_PATH)
	
clean-pyc:
	@find . -name '*.pyc' -delete
	@find . -name '*.pyo' -delete

develop:
	@virtualenv $(WORKON)/$(PROJECT_NAME)
	@. $(WORKON)/$(PROJECT_NAME)/bin/activate
	@pip install --user -r requirements.txt