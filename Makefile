all: clean test

flake:
	flake8 db  # TODO don't forget add other directories
	if ! isort -c -rc db tests; then \
		echo "Import sort errors, run 'make isort' to fix them!!!"; \
		isort --diff -rc db tests; \
		false; \
	fi

isort:
	isort -rc db  # TODO don't forget add other directories
	isort -rc tests

test: flake
	python -m pytest

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f `find . -type f -name '*.egg-info' `
	rm -f .coverage
	rm -rf coverage
	rm -rf cover
	rm -rf htmlcov
	rm -rf .cache
	rm -rf .eggs
	rm -rf .env

.PHONY: all clean flake test
