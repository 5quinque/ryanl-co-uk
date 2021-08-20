# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000/tcp

CMD ["gunicorn", "ryanl.wsgi", "--log-file", "-", "-b", "0.0.0.0:5000"]
