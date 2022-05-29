from glob import escape
import pika
from dotenv import load_dotenv
from os import path, environ
from elasticsearch import Elasticsearch, exceptions
import json
from time import sleep


IDEA_STATE_CREATE = 'CREATE'
IDEA_STATE_UPDATE = 'UPDATE'
IDEA_STATE_DELETE = 'DELETE'

global es


def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    print("Message received!")
    print("Received: ", body)
    data = json.loads(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if data['state'] == IDEA_STATE_CREATE:
        es.index(index='idea',
                 id=data['_id'],
                 body={'idea_name': data['idea_name']},
                 request_timeout=10)
    elif data['state'] == IDEA_STATE_UPDATE:
        es.index(index='idea',
                 id=data['_id'],
                 body={'idea_name': data['idea_name']},
                 request_timeout=10)
    elif data['state'] == IDEA_STATE_DELETE:
        es.delete(index='idea',
                  id=data['_id'])
    else:
        pass


def connect_elasticsearch(**kwargs):
    sleep(5)
    es = None
    while 1:
        try:
            es = Elasticsearch(
                "http://elasticsearch.search-service_prova:9200")
        except Exception as e:
            print("Can't connect to Elasticsearch: ", e)
            continue
        else:
            print("Connected to Elasticsearch", es.ping())
        break
    return es


def connect_rabbitmq():
    conn = None
    while 1:
        try:
            conn = pika.BlockingConnection(
                pika.URLParameters(environ.get(
                    'RABBITMQ_URI')))
        except Exception as e:
            print("Can't connect to Rabbitmq: ", e)
            continue
        else:
            print("Connected to Rabbitmq")
        break
    return conn


def main():
    global es
    es = connect_elasticsearch()
    connection = connect_rabbitmq()
    queue = 'index-seach-idea'
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.exchange_declare(
        exchange="idea",
        exchange_type="direct"
    )
    channel.queue_bind(
        exchange="idea",
        queue=queue,
        routing_key="idea.index")
    channel.basic_consume(queue, handle_delivery)

    print('Subscribed to ' + queue + ', waiting for messages...')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        connection.close()


if __name__ == '__main__':
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))

    main()
