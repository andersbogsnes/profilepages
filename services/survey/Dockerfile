FROM python:3.6

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]