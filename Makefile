test:
	nosetests -w . --no-byte-compile --cover-erase --with-coverage --cover-html --cover-html-dir=tests/reports

install:
	pip install -r requirements.txt