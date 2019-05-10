# Resource management

Example resource management

## Available endpoints


- `/api/`
  - The schema for asset objects
  - Supports: `POST` (new), `GET` (get all asset)

- `/api/asset/<id>`
  - Edit a asset in details
  - Supports: `PUT` (update), `DELETE` (delete the object with id)


## Installation 

You need to have `pipenv` installed in order to get the dependencies of this project. 

To do so, either install it via your package manager or use:

```bash
pip install pipenv

# install all dependencies (will initiate a new virtualenvironment)
pipenv install
```

If you're having issues with the dependencies, just run:

```
pipenv lock --pre --clear
pipenv install
```


## Running

Once everything is installed, run locally by using:

```
python run.py
```

## Running with Docker

Build a docker image with the provided Dockerfile by first building it:

```
docker build --rm -t flask-restsvc .
```

Then run the service, exposing port 8000:

```
docker run -d -p 8000:8000 flask-restsvc
```

## Configuration

In order to configure the service, the `app/config/__init__.py` should be modified with various options accepted by Flask.