#!/bin/bash

docker pull ghcr.nju.edu.cn/harrilee/cpt-fe-2024:production

# Stop the current container
docker stop cpt-be || true
docker rm cpt-be || true

# Start a new container with the latest image
docker run  \
  -e "CORS_ALLOWED_ORIGINS=$CORS_ALLOWED_ORIGINS" \
  -e "DB_HOST=$DB_HOST" \
  -e "DB_NAME=$DB_NAME" \
  -e "DB_PORT=$DB_PORT" \
  -e "DB_USER=$DB_USER" \
  -e "ALIYUN_ACCESS_KEY_ID=$ALIYUN_ACCESS_KEY_ID" \
  -e "ALIYUN_ACCESS_SECRET=$ALIYUN_ACCESS_SECRET" \
  -e "DB_PASSWORD=$DB_PASSWORD" \
  -e "ENCRYPTION_SALT=$ENCRYPTION_SALT" \
  -e "SECRET_KEY=$SECRET_KEY" \
  -d --name cpt-be -p 8000:8000 ghcr.nju.edu.cn/harrilee/cpt-be-2024:production