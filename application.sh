#!/bin/bash

FOLDER=$(dirname "$0")
export BUCKET=${FOLDER}/.pytest_cache
export PUB=${BUCKET}/secret/pub.pem
export KEY=${BUCKET}/secret/key.pem

mkdir -p "${BUCKET}"/secret
if [[ ! -f "${PUB}" ]] && [[ ! -f "${KEY}" ]]; then
  openssl req -x509 -newkey rsa:4096 -nodes -out "${PUB}" -keyout "${KEY}"
fi

python3 "${FOLDER}"/manage.py
