#!/usr/bin/env python
import pika
import sys
from get_conf import rabbitmq_conf

credentials = pika.PlainCredentials(rabbitmq_conf.get("user_name"), rabbitmq_conf.get("password"))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_conf.get("host"),port=rabbitmq_conf.get("port"), virtual_host=rabbitmq_conf.get("virtual_host"), credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()
