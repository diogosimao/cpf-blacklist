#!/usr/bin/env bash
# stop server

export DOCKER_CONFIG=${DOCKER_CONFIG:-docker-compose.yml}
docker-compose -f $DOCKER_CONFIG stop
echo "stopped"