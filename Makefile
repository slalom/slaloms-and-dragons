run:
	pipenv run python go.py
	
lint:
	pipenv run pycodestyle --first *.py