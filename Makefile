LOGGER  = /tmp/vaskaktusz/gungnir.log
PYTHON := $(shell which python3.12)
RUNNER  = ${PYTHON} ${CURDIR}/manage.py >> ${LOGGER} 2>&1

all: clean package deploy

clean:
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -xf ${LOGGER}
	crontab -r || echo "No crontab found for this user."

package: requirements.txt
	${PYTHON} -m pip install -r requirements.txt --break-system-packages

deploy: manage.py
	echo "*/30 * * * * ${RUNNER}" | crontab -
	nohup ${RUNNER} &