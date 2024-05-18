FOLDER := /tmp/vaskaktusz
PYTHON := $(shell which python3.12)
RUNNER := ${PYTHON} ${CURDIR}/manage.py >> ${FOLDER}/gungnir.log 2>&1

all: clean package deploy

clean:
	mkdir -p ${FOLDER}
	kill $(shell lsof -ti :${port}) || echo "No process with this PID."
	crontab -r || echo "No crontab found for this user."

package: requirements.txt
	${PYTHON} -m pip install -r requirements.txt --break-system-packages

deploy: manage.py
	echo "*/30 * * * * ${RUNNER}" | crontab -
	nohup ${RUNNER} &