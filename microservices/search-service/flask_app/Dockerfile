FROM python:3-alpine

# layer caching for faster builds
COPY requirements.txt /
RUN \
 python3 -m pip install -r requirements.txt --no-cache-dir 

ENV PYTHONUNBUFFERED=1

ADD . /flask_app
WORKDIR /flask_app


ENV FLASK_ENV=development

CMD python3 app.py

