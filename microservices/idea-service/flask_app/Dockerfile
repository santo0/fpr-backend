FROM python:3-alpine

# layer caching for faster builds
COPY requirements.txt /
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

#COPY app.py /app.py
ADD . /flask_app
WORKDIR /flask_app

ENV FLASK_ENV=development

CMD python3 app.py

#CMD gunicorn --workers $WORKERS \
#  --threads $THREADS \
#  --bind 0.0.0.0:$PORT_APP \
#  --log-level DEBUG \
#  app:app