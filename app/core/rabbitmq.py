import pika
from app.core.config import settings

def get_rabbitmq_connection():
    connection = pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
    return connection

def create_channel():
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    return channel
