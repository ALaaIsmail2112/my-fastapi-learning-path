
from sqlalchemy.orm import Session 
from .. import models , database , schema
from fastapi import Response , HTTPException , status


def get_all( db:Session ):
    blogs = db.query(models.BlogModel).all()
    return blogs

def ctreateBlog(request, db:Session ):
    new_blog = models.BlogModel(title = request.title , body = request.body,user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog(id ,response:Response , db):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id).first()
    # handling error is blog not found using http response and status 
    # if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {'msg': f'blog with id {id} is not found'}

    # handling error is blog not found using http Exception and status 
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'blog with id {id} is not found')

    return blog



def delete_blog(id ,  db:Session ):
    print(id)
    blog= db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'blog with id {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    
    return 'done'


def update_blog(id , request , db:Session ):
    blog = db.query(models.BlogModel).filter(models.BlogModel.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'blog with id {id} is not found')
    blog.update({'title':request.title , 'body':request.body})
    db.commit()
    return 'updated'