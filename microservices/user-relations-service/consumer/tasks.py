import pika
from dotenv import load_dotenv
from os import path, environ
from neo4j import GraphDatabase
import json
from time import sleep
from service.user_relations_service import UserRelationsService

IDEA_STATE_CREATE = 'CREATE'
IDEA_STATE_UPDATE = 'UPDATE'
IDEA_STATE_DELETE = 'DELETE'

global graph_db


def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    print("Message received!")
    print("Received: ", body)
    data = json.loads(body)
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if data['state'] == IDEA_STATE_CREATE:
        print('Create user relation with idea')
        print('Send message to search service')
        channel.exchange_declare(
            exchange='idea',
            exchange_type='direct'
        )
        channel.basic_publish(
            exchange='idea',
            routing_key='idea.index',
            body=body)
    elif data['state'] == IDEA_STATE_UPDATE:
        print('Modify user relation with idea')
        print('Send message to search service')
        channel.exchange_declare(
            exchange='idea',
            exchange_type='direct'
        )
        channel.basic_publish(
            exchange='idea',
            routing_key='idea.index',
            body=body)
    elif data['state'] == IDEA_STATE_DELETE:
        print('Delete user relation with idea')
        print('Send message to search service')
        channel.exchange_declare(
            exchange='idea',
            exchange_type='direct'
        )
        channel.basic_publish(
            exchange='idea',
            routing_key='idea.index',
            body=body)
    else:
        pass


def connect_neo4j():
    conn = None
    while 1:
        try:
            conn = GraphDatabase.driver(
                'bolt://localhost:7687', auth=('neo4j', 'mypass'))
        except Exception as e:
            print("Can't connecto to Neo4J: ", e)
            sleep(3)
            continue
        else:
            print("Connected to Neo4J")
            break
    return conn


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
    global graph_db
    graph_db = UserRelationsService(connect_neo4j())
    connection = connect_rabbitmq()
    queue = 'user-relation-idea'
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.exchange_declare(
        exchange="idea",
        exchange_type="direct"
    )
    channel.queue_bind(
        exchange="idea",
        queue=queue,
        routing_key="idea.operation")
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
