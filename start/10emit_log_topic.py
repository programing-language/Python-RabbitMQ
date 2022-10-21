#!/usr/bin/env python
import pika
import sys
from get_conf import rabbitmq_conf

credentials = pika.PlainCredentials(rabbitmq_conf.get("user_name"), rabbitmq_conf.get("password"))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_conf.get("host"),port=rabbitmq_conf.get("port"), virtual_host=rabbitmq_conf.get("virtual_host"), credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
