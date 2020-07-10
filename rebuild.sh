#!/bin/bash
sudo docker system prune -f
sudo docker-compose down
sudo docker-compose build
sudo docker-compose up
