#Dockerfile for content
FROM python:3.8.10

LABEL version=1.0.0

RUN mkdir /Content

WORKDIR /Content

COPY . /Content

EXPOSE 8003

RUN pip install -r requirements.txt && pip3 install --trusted-host pypi.python.org requests

VOLUME [/var/lib/docker/volumes/content_volume]
