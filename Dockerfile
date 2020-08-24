#base img and maintainer
FROM python:3.7-alpine
MAINTAINER Yuvi

#required for py docker since the output needs to be unbuffered
ENV PYTHONUNBUFFERED 1

#install dependencies from local req file to docker img's req
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#dir within img to store source code; copies source from local machine
RUN mkdir /app
WORKDIR /app
COPY ./app /app

#add user that will run the app using docker
RUN adduser -D user
USER user
