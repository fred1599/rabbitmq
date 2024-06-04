import pika
from app.core.rabbitmq import create_channel

def callback(ch, method, properties, body):
    print(f"Received {body}")

def consume():
    channel = create_channel()
    channel.queue_declare(queue='my_queue')
    channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
