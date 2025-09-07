# Build a Docker Image for FastAPI

## Package Requirements

#### For example, your requirements.txt could look like :
        fastapi[standard]>=0.113.0,<0.114.0
        pydantic>=2.7.0,<3.0.0

####  And you would normally install those package dependencies with pip, for example:

        pip install -r requirements.txt

### Create the FastAPI Code

Create an app directory and enter it.
Create an empty file __init__.py.
Create a main.py file with:
        from typing import Union
        from fastapi import FastAPI

        app = FastAPI()
        @app.get("/")
        def read_root():
            return {"Hello": "World"}


        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: Union[str, None] = None):
            return {"item_id": item_id, "q": q}

### Dockerfile
###### Now in the same project directory create a file Dockerfile with:



        FROM python:3.9


        WORKDIR /code


        COPY ./requirements.txt /code/requirements.txt


        RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


        COPY ./app /code/app


        CMD ["fastapi", "run", "app/main.py", "--port", "80"]


### ✅ Exec form:
### ✅ Do this
CMD ["fastapi", "run", "app/main.py", "--port", "80"]

## Directory Structure

    .
    ├── app
    │   ├── __init__.py
    │   └── main.py
    ├── Dockerfile
    └── requirements.txt


## Build the Docker Image
***docker build -t myimage .***

## Start the Docker Container
***docker run -d --name mycontainer -p 80:80 myimage***

## Check it

 http://127.0.0.1/items/5?q=somequery


**You will see something like:**

{"item_id": 5, "q": "somequery"} 


## Interactive API docs

 http://127.0.0.1/docs


 ****it is Done****