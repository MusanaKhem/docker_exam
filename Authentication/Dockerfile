#Dockerfile for authentication
FROM python:3.8.10

LABEL version=1.0.0

RUN mkdir /Authentication

WORKDIR /Authentication

COPY . /Authentication

EXPOSE 8001

RUN pip install -r requirements.txt && pip3 install --trusted-host pypi.python.org requests

VOLUME [var/lib/docker/volumes/authentication_volume]
