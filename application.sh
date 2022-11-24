#!/bin/bash

FOLDER=$(dirname "$0")
export BUCKET=${FOLDER}/.pytest_cache
SECRET=${BUCKET}/secret
PUB=${SECRET}/pub.pem
KEY=${SECRET}/key.pem

mkdir -p "${SECRET}"
if [[ ! -f "${SECRET}"/secret.dmg ]]; then
  openssl req -x509 -newkey rsa:4096 -nodes -out "${PUB}" -keyout "${KEY}"
  hdiutil create -encryption -stdinpass -srcfolder "${SECRET}" "${SECRET}"/secret.dmg
  rm "${PUB}"
  rm "${KEY}"
fi

VOLUME=/Volumes/secret
export PUB=${VOLUME}/pub.pem
export KEY=${VOLUME}/key.pem

if [[ ! -d ${VOLUME} ]]; then
  hdiutil attach -stdinpass "${SECRET}"/secret.dmg
fi

python3 "${FOLDER}"/manage.py
