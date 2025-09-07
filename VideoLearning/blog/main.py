from fastapi import FastAPI 
from . import  models 
# from . hashing import Hashing
from .database import engine 
from .routers import users , blogs , authentication



# to run this ... uvicorn blog.main:app --reload
app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(blogs.router)

# Connect Dtatbase 
# first what is ORM 
#Orm IS object relational Mapping ... it is a way to connect to database using object oriented programming
# like sqlalchemy is a orm  ... convert data to object and object to data




