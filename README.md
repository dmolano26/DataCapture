# Data Capture Application

Data Capture with Python

# Local environment

## Local environment with pipenv

### Install dependencies

1. Install `pyenv` (https://github.com/pyenv/pyenv-installer) and `pipenv` (https://pipenv.pypa.io/en/latest/)
2. Install Python version 3.9.{x} (`pyenv install 3.9.13`).
3. Clone the project
5. Create an virtualenv and install dependencies using `pipenv shell && pipenv install -d`.

### Run the Application

You can run the application with

```sh
# inside root project path
python main.py
```

### Testing

```sh
# inside ./app folder
python -m unittest tests/test_main.py
```

### Flake8
```sh
flake8 --count --show-source --statistics
```

## Information
Any questions, please contact [dmolano](mailto:diego.molano25@gmail.com)
