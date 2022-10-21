#!/usr/bin/env python
import pika
from get_conf import rabbitmq_conf

credentials = pika.PlainCredentials(rabbitmq_conf.get("user_name"), rabbitmq_conf.get("password"))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbitmq_conf.get("host"),port=rabbitmq_conf.get("port"), virtual_host=rabbitmq_conf.get("virtual_host"), credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
