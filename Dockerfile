FROM python:3.12-slim

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY . .

RUN poetry install --no-root

CMD ["poetry", "run", "python"]
