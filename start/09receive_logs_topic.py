#!/usr/bin/env python
import pika
import sys
from get_conf import rabbitmq_conf

credentials = pika.PlainCredentials(rabbitmq_conf.get("user_name"), rabbitmq_conf.get("password"))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_conf.get("host"),port=rabbitmq_conf.get("port"), virtual_host=rabbitmq_conf.get("virtual_host"), credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
