from fastapi import APIRouter , status , Depends , HTTPException
from .. import schema , database , models , hashing
from sqlalchemy.orm import Session
from ..repository import user


router = APIRouter(
    # tags and prefix ... make our code clean an easy
    # Router Parametrs 
    tags=['users'],
    prefix = '/user'
)



##################### Authentication #####################

# Hashing password 

# Create User
@ router.post('/', status_code=status.HTTP_201_CREATED )
def create_user(request:schema.user ,db:Session = Depends(database.get_db) ):

    return user.create_user(request , db)

@ router.get('/'  ,status_code=status.HTTP_200_OK ,  response_model=list[schema.showUser] )
def get_all_user(db:Session = Depends(database.get_db)):
    return user.get_all_user(db)


@ router.get('/{id}'  ,status_code=status.HTTP_200_OK ,  response_model=schema.showUser )
def get_user(id:int , db:Session = Depends(database.get_db)):
    return user.get_user(id,db)


 # fourth path ... delete Blog
@ router.delete('/user/{id}' , status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int ,  db:Session = Depends(database.get_db)):
    return user.delete_user(id , db)