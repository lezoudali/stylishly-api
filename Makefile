all: clean test-db

flake:
	flake8 --exclude db/migrations db stylishly tests
	if ! isort -c -rc db stylishly tests; then \
		echo "Import sort errors, run 'make isort' to fix them!!!"; \
		isort --diff -rc db tests stylishly; \
		false; \
	fi

isort:
	isort -rc db
	isort -rc stylishly
	isort -rc tests

test-db: flake
	python -m pytest -s --quiet tests/db

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

.PHONY: all clean flake test-db
