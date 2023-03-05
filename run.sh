#!/bin/bash
docker stop app
docker rm app
docker rmi app:v0
docker build --network=host -t app:v0 .