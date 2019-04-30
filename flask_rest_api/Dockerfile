FROM python:3-alpine

MAINTAINER Marko  "marko.lubarda@integrationalpha.com"

RUN mkdir -p /var/www/app
RUN apt-get install

WORKDIR /var/www/app

COPY requirements.txt /var/www/app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /var/www/app

RUN python3 setup.py develop

CMD python3 rest_api_demo/app.py
