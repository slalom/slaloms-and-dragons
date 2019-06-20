run:
	pipenv run python -m game
	
lint:
	pipenv run black .

test:
	pipenv run python -m unittest discover -s tests/ -p "*_test.py"