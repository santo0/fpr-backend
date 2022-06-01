import pika
from dotenv import load_dotenv
from os import path, environ
from elasticsearch import Elasticsearch
import json
from time import sleep
from service.search_service import SearchService

IDEA_STATE_CREATE = 'CREATE'
IDEA_STATE_UPDATE = 'UPDATE'
IDEA_STATE_DELETE = 'DELETE'

global search_engine


def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    print("Message received!")
    print("Received: ", body)
    data = json.loads(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if data['state'] == IDEA_STATE_CREATE:
        search_engine.index_idea(data['id'], data['idea_name'])
    elif data['state'] == IDEA_STATE_UPDATE:
        search_engine.index_idea(data['id'], data['idea_name'])
    elif data['state'] == IDEA_STATE_DELETE:
        search_engine.delete_index('idea', data['id'])
    else:
        pass


def connect_elasticsearch(**kwargs):
    es = None
    while 1:
        try:
            es = Elasticsearch(
                "http://elasticsearch.search-service_default:9200")
        except Exception as e:
            print("Can't connect to Elasticsearch: ", e)
            sleep(3)
            continue
        else:
            print("Elasticsearch has been found")
            if es.ping():
                print("Connected to Elasticsearch", es.ping())
                break
            else:
                print("Can't ping to Elasticsearch")
                sleep(3)
                continue
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
            sleep(3)
            continue
        else:
            print("Connected to Rabbitmq")
        break
    return conn


def main():
    global search_engine
    search_engine = SearchService(connect_elasticsearch())
    connection = connect_rabbitmq()
    queue = 'index-search-idea'
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
