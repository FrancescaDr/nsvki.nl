FROM python:alpine

WORKDIR /app

# Python
COPY requirements.txt ./requirements.txt

# Install a virtual package with build dependencies voor pip install
RUN apk add -U --virtual build-deps python3-dev build-base linux-headers

RUN pip install uwsgi && \
    pip install -r requirements.txt

# Remove virtual package
RUN apk del build-deps

# Copy the source into the image for production
COPY . /app
RUN pybabel compile -d nsvki/translations

CMD uwsgi --ini uwsgi.ini

