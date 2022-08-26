FROM python:3.8.10-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk add build-base
RUN pip install --upgrade pip
RUN pip install -U setuptools pip
RUN pip install fastapi[all]
RUN pip install pymongo
RUN pip install motor
RUN pip install beanie