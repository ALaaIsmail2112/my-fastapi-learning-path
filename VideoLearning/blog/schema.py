from pydantic import BaseModel , ConfigDict
from typing import Optional 
"""
NOTE :
here we will discuss about schema using pydantic with response model
schema is used to define how the data should be sent over the network
and how the data should be received from the network
so in our case we will define how the blog data should be sent and received

example 
 response_model=schema.ShowBlog

"""


"""
NOTE :
 how to use pydantic as schema in fastapi to define what we want to return from database 
 **FIRST** 
 what different between pydantic model and sqlalchemy model
 1 - pydantic model is used to define how the data should be sent over the network
 2 - sqlalchemy model is used to define how the data should be stored in the database

"""

class Blog(BaseModel):
    title:str
    body:str
    

class user(BaseModel):
    name:str
    email:str
    password:str

# NOTE 
class showUser(BaseModel):
    name:str
    email:str
    blogs: list[Blog] = []   # user ممكن يكون عنده blogs كتير

    class Config:
        orm_mode=True

    # model_config = ConfigDict(from_attributes=True)



class ShowBlog(Blog):
    """
    NOTE :
    here we inherit from Blog class to avoid repetition of code
    """
    title:str
    body:str
    creator: Optional["showUser"]  # خليها optional عشان ممكن يكون blog مالوش user

    class Config:
        orm_mode = True
        """
        NOTE :
       pydantic it deals with data come from database as **dictionary** to apply validation and serialization
       but sqlalchemy return data as **object**
        """
"""
if we want to show specific things from class 
we put paramter BaseModel in method not class of this thing

###### error ######
class showUser(user): # this is where error  we put user not BaseModel 
    name:str
    email:str
    class config:
        orm_mode=True

"""


class login(BaseModel):
    email:str 
    password:str


#  this methodS is function of authentication by JWT
class Token(BaseModel):
    access_token:str
    token_type:str
#  this method is function of authentication by JWT
class TokenData(BaseModel):
    email:Optional[str]=None