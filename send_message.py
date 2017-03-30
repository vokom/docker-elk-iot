#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json
import random

MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60

def on_connect():
    pass

def on_message():
    pass

# Set up connection to MQTT
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE)

# Send value
client.publish('sensor', random.randrange(0, 100), qos=2)
