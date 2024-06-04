import pika
from app.core.config import settings

def send_message(content: str):
    connection_params = pika.URLParameters(settings.RABBITMQ_URL)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    queue_name = 'my_queue'
    channel.queue_declare(queue=queue_name)

    channel.basic_publish(exchange='', routing_key=queue_name, body=content)

    connection.close()
