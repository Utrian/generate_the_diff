install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

pytest:
	poetry run pytest

test-coverage:
	coverage run -m pytest tests

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=gendiff
