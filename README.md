## Python Project Template

```
# Note: Install Python 3

$: python -m pip install -U pip  # update pip, a package manager

$: pip install --user pipenv  # install pipenv, a dependency manager
# Note: you may need to add pipenv to PATH

$: pipenv install  # install all dependencies
```

### docs

```
$: pipenv shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
```

### src

```
$: pipenv run python ./src/big_package/runner.py
$: pipenv run
```

### tests

```
$: pipenv run pytest
```

```
$: pipenv run pytest --cov=src --cov-report=html tests
#: Note: the coverage report is htmlcov/index.html
```

### Pipfile/Pipfile.lock

Dependencies, Python version and the virtual environment are managed by pipenv.

```
$: pipenv --python Python-Version  # lock project's Python version

$: pip search Package-Name
$: pipenv install Package-Name==Package-Version
```

### setup.cfg

Configure Python libraries.

### setup.py

Define project entry point and metadata.

### Linters

```
$: pipenv run flake8  # check PEP8
```

### Enter venv

```
$: pipenv shell
```
