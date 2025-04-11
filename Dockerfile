FROM python:3.12.0-slim AS builder

RUN apt update -y && apt install -y build-essential libpq-dev gcc

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM python:3.12.0-slim AS final

RUN apt update -y && \
    apt install -y postgresql postgresql-contrib libpq-dev curl nano net-tools pgloader

WORKDIR /app

COPY --from=builder /app /app

RUN pgloader sqlite:///tmp/db.sqlite3 postgresql://elama:uhu.2024@localhost/esprolama

RUN rm -rf /app/db.sqlite3 /app/.dockerignore /app/requirements.txt 2> /dev/null

EXPOSE 8000

ENV DB_NAME=esprolama
ENV DB_USER=elama
ENV DB_PASSWORD=uhu.2024
ENV DB_HOST=localhost
ENV DB_PORT=5432

CMD ["service", "postgresql", "start", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]
