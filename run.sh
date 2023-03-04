#!/bin/bash
docker stop app
docker rm app
docker rmi app:v0
docker build --network=host -t app:v0 .
docker run --name app -p 80:80 -d app:v0