all: clean package install

clean:
	rm -rf .pytest_cache
	rm -rf __pycache__

package: requirements.txt
	${PYTHON} -m pip install -r requirements.txt --break-system-packages

install: manage.py
	${PYTHON} manage.py