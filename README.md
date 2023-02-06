# LSEG Challenge

## Project Structure:
```
.
├── data
│   ├── coding_challenge_input.txt
│   └── test_input.txt
├── lseg_challenge
│   ├── __init__.py
│   └── lightshow.py
├── tests
│   ├── __init__.py
│   └── test_lightshow.py
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Virtual Environments
### Install
To install runtime dependencies in a virtual environment:
```
poetry install
```

To install development dependencies in a virtual environment:
```
poetry install --with dev
```

### Run
To run the tests:
```
poetry run pytest
```

To run the application:
```
poetry run python app.py
```

## Docker
To build the image, run in project root:
```
docker build --pull --rm -f "Dockerfile" -t lsegchallenge:latest "."
```

To run the containerised application and inspect its output:
```
docker run -it lsegchallenge
```