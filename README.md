## Python Project Template

```
After creating a new git repository copy over:
* docs
* poetry_template
* tests
* pyproject.toml
* README.md

Go through the project and change the placeholder values. pyproject.toml contains the list of the most important values present throughout the project.

Finally, delete this note.
```

## Development

```
# Note: Install Python 3
# Update pip and install virtualenv (dependency encapsulator) and black (linter; IDE needs to be restarted)

# Note: install Poetry for Linux
$: curl -sSL https://install.python-poetry.org | python3 -

# Note: install Poetry for Windows
$: (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

$: curl -sSL https://install.python-poetry.org | python3 - --uninstall
$: (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --uninstall
```

```
# Note: `.toml` project name and package have to match (poetry-template; poetry_template)
$: poetry install  # install all dependencies
```

### dist

```
$: pip install dist/poetry_template-0.1.5-py3-none.any.whl

$: poetry-template
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### poetry_template

```
$: poetry run poetry-template --help
$: poetry run python ./poetry_template/runner.py --help

$: poetry run python ./poetry_template/runner.py -x 2 -y -1 -tuple A B C -list D -list E -list F -move rock
```

### tests

```
$: poetry run pytest --durations=0
```

```
$: poetry run pytest --cov=poetry_template --cov-report=html tests
# Note: see coverage report in htmlcov/index.html
# Note: exclude directories from coverage report through .coveragerc
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add [-D] Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.


### Linters

```
$: poetry run black .
```

### MyPy

```
$: poetry run mypy ./poetry_template ./tests
```

### cProfile

```
$: poetry run python ./poetry_template/profiler.py
```

### Build and publish

```
$: poetry build

# Note: get the token from your PiPy account
$: poetry config pypi-token.pypi PyPI-Api-Access-Token
```

```
$: poetry publish --build
```

```
https://pypi.org/project/poetry-template/
```
