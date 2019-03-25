run:
	pipenv run python -m game
	
lint:
	pipenv run autopep8 --in-place --aggressive --aggressive --recursive .

test:
	pipenv run python -m unittest discover -s tests/ -p "*_test.py"