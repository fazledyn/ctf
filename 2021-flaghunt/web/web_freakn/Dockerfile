FROM php:7.4-apache

WORKDIR /var/www/html


RUN apt-get update -y && apt-get install -y libmariadb-dev

RUN docker-php-ext-install mysqli

COPY src/ /var/www/html/