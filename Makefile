TEST_PATH=./tests

test: clean-pyc
#	@$(foreach file,$(SOURCES), python -m pytest $(file);)
	python -m pytest $(TEST_PATH)
	
clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete