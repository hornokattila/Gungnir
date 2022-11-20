#!/bin/bash

export BUCKET=$(dirname $0)/.pytest_cache
export PUB=${BUCKET}/newkey/pub.pem
export KEY=${BUCKET}/newkey/key.pem

mkdir -p ${BUCKET}/newkey
[ -f ${PUB} ] && [ -f ${KEY} ] || openssl req -x509 -newkey rsa:4096 -nodes -out ${PUB} -keyout ${KEY}

python3 manage.py
