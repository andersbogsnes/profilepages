#!/usr/bin/env bash

echo "Waiting for postgres"

while ! nc -z survey_db 5432; do
    sleep 0.1
done

echo "Postgres started"

gunicorn -b 0.0.0.0:5000 app.main:app --reload