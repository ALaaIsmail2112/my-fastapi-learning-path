from fastapi import FastAPI


app = FastAPI()

"""
📖 NOTE :
uvicorn main:app reload 
this reload will automatically reload the server when we make changes to the code

"""
@app.get('/') # without this path application will not start and witll give me error  // decorate
def start():
    # return "Starting the video learning application"
    return {'data':{'name':'alaa' , 'age':21}}


"""
📖 NOTE :
what is operations 
.... get 
.... put 
.... post
.... delete

('/') ...this is path
get ... this is path operation
start ... this is path operation method
@app ... path operation decorator

"""
# make routing


@app.get('/route') # this is called path 
def route():
    return {'data':{'message':'This is the route endpoint'}}



@app.get('/blog') # this is called path 
def blog():
    return {'data':'my fisrt blog'}


@app.get('/blog/unbublished')
def unbublished():
    return {'data':'unbublished blogs here '}

@app.get('/blog/{id}')
def show(id:int):
    # fetch blog with id =id
    return {'data':id}

@app.get('/blog/{id}/comments')
def showcomments(id):
    return {'data':{'1,2'}}


"""
📖 NOTE :
fastapi is reading code line by line so there is error if u handling method with id .. int and call after that the same path with string value 
**Example** 

@app.get('/blog/{id}')
def show(id:int):
    # fetch blog with id =id
    return {'data':id}


    @app.get('/blog/unbublished')
def unbublished():
    return {'data':'unbublished blogs here '}



# ⚠️ WARNING : will give me this erro
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "unbublished"
    }
  ]
}

"""


# ------------- Query Parameter ---------------------

"""
📖 NOTE : what is query parameter
Query parameters are a way to send additional information to the server as part of the URL. They are typically used to filter or sort data, or to provide additional context for a request.

"""

@app.get('/test')
def testqueryparameter(limit , published:bool):
    #use ...  http://127.0.0.1:8000/test?limit=10
    if published:
        return {'data':f'{limit} for query parametr' }
    else:
        return {'data':'no data found'}
    

"""
📖 NOTE ... if we give default value for each of query paramter we must also give to second one 
"""

@app.get('/test/{id}')
def testqueryparameter2(id,limit):
    #use ...  http://127.0.0.1:8000/test?limit=10
   return {'data':{id,limit} }
# fastapi is knowing difference between path parameter and query parameter by the position of the parameter in the function





# -------  Request Body -------

from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    publishedat: Optional[bool] = None # this is optional parameter [optional , None]

# -------------  Request Parameter ---------------------
@app.post('/blog')
def creatingblog(request:Blog):
    
    return {request.title , request.body , request.publishedat}


