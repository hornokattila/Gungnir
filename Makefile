all: clean package deploy

clean:
	rm -rf .pytest_cache
	rm -rf __pycache__

package: requirements.txt
	${PYTHON} -m pip install -r requirements.txt --break-system-packages

deploy: manage.py
	${PYTHON} manage.py