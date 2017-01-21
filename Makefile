flake:
	flake8 db  # TODO don't forget add other directories
	if ! isort -c -rc db tests; then \
		echo "Import sort errors, run 'make isort' to fix them!!!"; \
		isort --diff -rc db tests; \
		false; \
	fi

isort:
	isort rc db  # TODO don't forget add other directories
	isort rc tests

test: flake
	python -m pytest
