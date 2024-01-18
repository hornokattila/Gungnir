all: clean package deploy

clean:
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -xf ${LOGGER}

package: requirements.txt
	${PYTHON} -m pip install -r requirements.txt --break-system-packages

deploy: manage.py
	echo "*/5 * * * * ${PYTHON} ${CURDIR}/manage.py >> ${LOGGER} 2>&1" | crontab -