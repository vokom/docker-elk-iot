#!/usr/bin/env python

import pika
import json
import random

# Set up connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure that the exchange and queue are declared
channel.exchange_declare(exchange='data', type='fanout', durable=True)
channel.queue_declare(queue='sensor', durable=True)

# Send message
data = json.dumps({'message': random.randrange(0, 100)})
channel.basic_publish(exchange='data', routing_key='sensor', body=data)

# Close connection
connection.close()
