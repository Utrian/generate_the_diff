FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update; \
        \
        apt-get install make; \
        \
        pip install poetry; \
        poetry config virtualenvs.create false; \
        poetry install

CMD [ "bash" ]
