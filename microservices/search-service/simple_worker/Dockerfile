FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

# layer caching for faster builds
COPY requirements.txt /
RUN \
 apk add netcat-openbsd && \
 python3 -m pip install -r requirements.txt --no-cache-dir

#COPY app.py /app.py
ADD . /simple_worker
WORKDIR /simple_worker

ENTRYPOINT ["python3", "tasks.py"]

#-Q celery_worker
#ENTRYPOINT ['celery','-A','test_celery', 'worker', '--loglevel=info']