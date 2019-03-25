run:
	pipenv run python -m game
	
lint:
	pipenv run autopep8 --in-place --aggressive --aggressive *.py