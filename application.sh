#!/bin/bash

FOLDER=$(dirname "$0")
export BUCKET=${FOLDER}/.pytest_cache
export PUB=${BUCKET}/secret/pub.pem
export KEY=${BUCKET}/secret/key.pem

mkdir -p "${BUCKET}"/secret
if [[ ! -f "${BUCKET}"/secret/secret.dmg ]]; then
  openssl req -x509 -newkey rsa:4096 -nodes -out "${PUB}" -keyout "${KEY}"
  hdiutil create -encryption -stdinpass -srcfolder "${BUCKET}"/secret "${BUCKET}"/secret/secret.dmg
  rm "${PUB}"
  rm "${KEY}"
fi

if [[ ! -d /Volumes/secret ]]; then
  hdiutil attach -stdinpass "${BUCKET}"/secret/secret.dmg
fi

export PUB=/Volumes/secret/pub.pem
export KEY=/Volumes/secret/key.pem

python3 "${FOLDER}"/manage.py
