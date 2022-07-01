FROM python:3.9
# FROM huanjason/scikit-learn:latest
# ARG PYTHON_VERSION=3.9
MAINTAINER Moein Kameli

ENV PYTHONUNBU FFERED 1

RUN pip3 install \
        scipy \
        scikit-learn \
        pandas \
        matplotlib

# RUN apt update
# RUN apt-get update
# RUN apt-get -y install python3.9


# RUN python -m pip install --upgrade "pip < 19.2"
#
# RUN python -m pip install --upgrade "pip < 21.0"

# RUN pip install -U sklearn
# RUN pip install -U joblib

# RUN pip freeze && python --version && pip --version && pip sag

RUN pip install 'imbalanced-learn>=0.9,<1.2'


# RUN apk add --no-cache --update \
#     python3 python3-dev \
#     libffi-dev openssl-dev \
#     libxml2 libxml2-dev \
#     libxslt libxslt-dev \
#     libjpeg-turbo-dev zlib-dev \
#     libstdc++
#
# RUN apk add --no-cache --virtual \
#     g++ gcc gfortran \
#     musl-dev lapack-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser user
USER user