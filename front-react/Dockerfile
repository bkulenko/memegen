FROM ubuntu:18.04

WORKDIR /app

COPY . /app

RUN apt-get update
RUN apt-get install npm -y

EXPOSE 3000

RUN npm start 0.0.0.0