#!/usr/bin/env python
import pika
from get_conf import rabbitmq_conf

credentials = pika.PlainCredentials(rabbitmq_conf.get("user_name"), rabbitmq_conf.get("password"))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_conf.get("host"),port=rabbitmq_conf.get("port"), virtual_host=rabbitmq_conf.get("virtual_host"), credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
