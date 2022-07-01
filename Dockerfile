FROM python:3.9

MAINTAINER Moein Kameli

ENV PYTHONUNBU FFERED 1

RUN pip3 install \
        scipy \
        scikit-learn \
        pandas \
        matplotlib

RUN pip install 'imbalanced-learn>=0.9,<1.2'

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user