install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 engine

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=engine --cov-report xml

coverage-missing:
	poetry run pytest --cov-report term-missing --cov=engine
