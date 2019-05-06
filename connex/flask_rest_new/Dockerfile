FROM python:3-alpine

MAINTAINER Marko  "marko.lubarda@integrationalpha.com"

RUN mkdir -p /var/www/app

WORKDIR /var/www/app

RUN apk add nginx \
        gcc libc-dev linux-headers supervisor

RUN pip3 install uwsgi


COPY requirements.txt /var/www/app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY nginx.conf /etc/nginx/
COPY flask-site-nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/

COPY . /var/www/app

RUN python3 setup.py develop

CMD ["/usr/bin/supervisord"]