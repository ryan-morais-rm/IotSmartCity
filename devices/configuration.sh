#!/bin/bash

# Image build and execution
docker build -t iot-flask-app .
docker run -d --name iot-flask --network iot-net -p 5000:5000 iot-flask-app
