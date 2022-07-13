FROM python:3.9

MAINTAINER Moein Kameli

ENV PYTHONUNBU FFERED 1

RUN apt update
RUN apt install nginx

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user