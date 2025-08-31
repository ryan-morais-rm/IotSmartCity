#!/bin/bash

# Image build and execution
docker build -t iot-flask-app .
docker run -p 5000:5000 iot-flask-app
docker run -d -p 5000:5000 iot-flask-app