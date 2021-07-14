install-dev-deps: dev-deps
	pip-sync requirements.txt dev-requirements.txt

install-deps: deps
	pip-sync requirements.txt

deps:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in

dev-deps: deps
	pip-compile dev-requirements.in

run:
	cd src && python app.py

lint:
	black --skip-string-normalization src && flake8 src

test:
	cd src && pytest -v
