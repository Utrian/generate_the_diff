install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: all gendiff clean
gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest
	poetry run pytest --cov=gendiff --cov-report xml
	poetry run pytest --cov-report term-missing --cov=gendiff
