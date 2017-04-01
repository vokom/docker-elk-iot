#!/usr/bin/env bash

mosquitto_pub -t sensor -m "{\"type\": \"test\", \"message\": 52}"