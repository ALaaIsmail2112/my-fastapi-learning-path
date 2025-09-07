from fastapi import APIRouter , status , Depends , HTTPException , Response
from .. import schema , database , models , hashing , oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
     # here we can tags here rather than in path 
    tags=['blogs'],
    prefix='/blog'
)

 # First path ... create Blog
@ router.post('/' , status_code=status.HTTP_201_CREATED )
def ctreateBlog(request: schema.Blog , db:Session = Depends(database.get_db),current_user: schema.user = Depends(oauth2.get_current_user)):
    
    return blog.ctreateBlog(request , db)



 # second path ... get all Blog    # done blog and user Repository 




@ router.get('/' , status_code=status.HTTP_200_OK , response_model=list[schema.ShowBlog])
def get_all( db:Session = Depends(database.get_db) , current_user: schema.user = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

"""
NOTE:
when we return blog it give use three things , id , title , body 
but we want to return only title and body not id
    so we use pydantic **Schema** to define what we want to return
    Using Respone Model
    we will create schema.py file in blog folder
"""
 # third path ... get Blog of specific id and handle error if blog not found 
@ router.get('/{id}' , status_code=status.HTTP_200_OK , response_model=schema.ShowBlog)
def get_blog(id:int ,response:Response , db:Session = Depends(database.get_db) , current_user: schema.user = Depends(oauth2.get_current_user)):
    return blog.get_blog(id ,response, db)

 # fourth path ... delete Blog



@ router.delete('/{id}' , status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int ,  db:Session = Depends(database.get_db) , current_user: schema.user = Depends(oauth2.get_current_user)):
    return blog.delete_blog(id, db)



 # fifthpath ... upadate Blog



@ router.put('/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int , request:schema.Blog , db:Session = Depends(database.get_db) , current_user: schema.user = Depends(oauth2.get_current_user)):
    return blog.update_blog(id,request , db)
