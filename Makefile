run:
	pipenv run python go.py
	
lint:
	pipenv run autopep8 --in-place --aggressive --aggressive *.py