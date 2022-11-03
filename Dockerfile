# # syntax=docker/dockerfile:1

FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# ADD GOOGLE API KEY HERE
ENV PLACES_API "<api_key>"

# Set work directory
WORKDIR /CITS3200

RUN pip install gdal

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy porject
COPY . /CITS3200/

# collect static files
RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn foodAtlas.wsgi:application --bind 0.0.0.0:$PORT