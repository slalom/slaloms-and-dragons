![alt text](https://github.com/slalom/slaloms-and-dragons/blob/master/logo.png)

### Prereqs

- Python 3.6.5+
- pipenv (setup `pipenv` (https://pypi.org/project/pipenv/) )

### Running

1. `pipenv install`
2. `make run`

### Testing

`make test`

### Styling
using `autopep8` (https://pypi.org/project/autopep8/) to automatically format Python code to conform to the PEP 8 style guide. 

Run `make lint`  to conform to the PEP 8 style guide.

### Tips
- Create virtual environment on Mac OS (Assuming you have already installed Python3)
    - python3 -m venv <name of environment> ``` python3 -m venv venv ```
