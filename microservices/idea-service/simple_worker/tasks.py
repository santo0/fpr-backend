import pika


def handle_delivery(channel, method, header, body):
    """Called when we receive a message from RabbitMQ"""
    print("Message received!")
    print("Received: ", body)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():    
    return
    connection_params = pika.ConnectionParameters(
        host='amqp://admin:mypass@127.0.0.1:5672')
    connection = pika.BlockingConnection(connection_params)
    queue = 'index-seach-idea'
    channel = connection.channel()
    channel.queue_declare(queue=queue)
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
    main()

