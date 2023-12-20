#Dockerfile for authorization

FROM python:3.8.10

LABEL version=1.0.0

RUN mkdir /Authorization

WORKDIR /Authorization

COPY . /Authorization

EXPOSE 8002

RUN pip install -r requirements.txt && pip3 install --trusted-host pypi.python.org requests

VOLUME [var/lib/docker/volumes/authorization_volume]
