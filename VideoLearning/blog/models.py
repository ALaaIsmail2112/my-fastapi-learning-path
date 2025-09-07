from .database import Base
from sqlalchemy import Column, Integer , String , ForeignKey
# define Relationship 
from sqlalchemy.orm import relationship


class BlogModel(Base):
        __tablename__ = 'blogs'
        id = Column(Integer , primary_key=True , index=True)
        title = Column(String)
        body = Column(String)
        # define Relationship 
        user_id = Column(Integer , ForeignKey('user.id'))
        creator = relationship("UserModel"  , back_populates='blogs')


class UserModel(Base):
        __tablename__ = 'user'
        id = Column(Integer , primary_key=True , index=True)
        name = Column(String)
        email = Column(String , unique=True , index=True)
        password = Column(String)
        # define Relationship 
        blogs = relationship('BlogModel' , back_populates='creator')

