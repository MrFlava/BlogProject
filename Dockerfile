FROM python:3.8-alpine
MAINTAINER mrflava <thatelitemaili33t@gmail.com>

# Installing git
RUN apk add git

RUN mkdir /main
COPY . /main
WORKDIR /main/

COPY requirements.txt /code/
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
