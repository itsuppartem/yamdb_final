FROM python:3.7-slim

WORKDIR /api_yamdb


COPY requirements.txt /api_yamdb

RUN pip3 install -r /api_yamdb/requirements.txt --no-cache-dir

COPY . /api_yamdb


CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 