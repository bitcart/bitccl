all: ci

lint:
	flake8

checkformat:
	black --check .
	isort --check .

format:
	black .
	isort .

test:
	pytest tests/ $(TEST_ARGS)

ci: checkformat lint test
