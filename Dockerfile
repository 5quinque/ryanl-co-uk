# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# RUN pipenv run python manage.py migrate 

EXPOSE 80/tcp

CMD ["gunicorn", "ryanl.wsgi", "--log-file", "-", "-b", "0.0.0.0:80"]
