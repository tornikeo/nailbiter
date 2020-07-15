#!/usr/bin/env bash

# Use ./rebuild.bash [target]
# Target can be :
# tf_serving
# web
# or empty to build both
TARGET=$1
docker system prune -f
docker-compose up -d --no-deps --build $TARGET