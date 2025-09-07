from sqlalchemy import create_engine
# create_engine: ده المسؤول عن إنشاء الاتصال بقاعدة البيانات.
# بيحدد نوع قاعدة البيانات (SQLite, MySQL, PostgreSQL) وبيتعامل معها تحت الغطاء.
from sqlalchemy.ext.declarative import declarative_base
# declarative_base(): ده بيوفر Base class للكلاسات اللي هتمثل الجداول.
# أي جدول هتعمله في قاعدة البيانات، هتعمله ككلاس بيرث من Base.
from sqlalchemy.orm import sessionmaker
# sessionmaker: ده المسؤول عن إنشاء جلسة (Session) للتعامل مع قاعدة البيانات.
# الـ Session هو اللي بيخلي الكود يقرأ أو يكتب في قاعدة البيانات

SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})


sessionlocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = sessionlocal()

    try:
        yield db
    finally:
        db.close()
