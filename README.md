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

> [!WARNING]
> The `/image-hasher` endpoint will eat about 10G of your RAM!

To run the application just run:

```shell
$ PYTHONPATH=$(pwd)/src uvicorn sre.main:app
```

Then just hit `http://localhost:8000/docs` to see the OpenAPI docs.
