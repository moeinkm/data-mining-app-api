FROM frolvlad/alpine-python-machinelearning:latest
MAINTAINER Moein Kameli

ENV PYTHONUNBU FFERED 1

# RUN apk add --no-cache --update \
#     python3 python3-dev \
#     libffi-dev openssl-dev \
#     libxml2 libxml2-dev \
#     libxslt libxslt-dev \
#     libjpeg-turbo-dev zlib-dev \
#     libstdc++

# RUN apk add --no-cache --virtual \
#     g++ gcc gfortran \
#     musl-dev lapack-dev

# RUN pip install scipy

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user