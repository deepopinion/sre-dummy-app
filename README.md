# sre-dummy-app

Dummy app to use with SRE challenge

## Setting up

This project works with Python 3.12+

1. Create a Python virtual environment and activate it
2. Install the dependencies: `pip install -r requirements.txt`

## Testing

To test this project just run:

```shell
$ pytest tests/
```

## Running

To run the application just run:

```shell
$ PYTHONPATH=$(pwd)/src uvicorn sre.main:app
```
