#base img and maintainer
FROM python:3.7-alpine
MAINTAINER Yuvi

#required for py docker since the output needs to be unbuffered
ENV PYTHONUNBUFFERED 1

#install dependencies from local req file to docker img's req
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

#dir within img to store source code; copies source from local machine
RUN mkdir /app
WORKDIR /app
COPY ./app /app

#add user that will run the app using docker
RUN adduser -D user
USER user
