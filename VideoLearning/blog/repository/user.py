
from sqlalchemy.orm import Session 
from .. import models , database , schema , hashing
from fastapi import Response , HTTPException , status


def create_user(request:schema.user ,db:Session  ):
    new_user= models.UserModel(name=request.name , email=request.email,password=hashing.Hashing.bcrypt(request.password))
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db:Session):
    users = db.query(models.UserModel).all()
    return users


def get_user(id , db:Session):
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="this user deoes't exist")
    return user



def delete_user(id,  db:Session):
    print(id)
    USER= db.query(models.UserModel).filter(models.UserModel.id == id)
    if not USER.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'user with id {id} is not found')
    USER.delete(synchronize_session=False)
    db.commit()