# 🚨 Known Errors & Fixes

This document lists common errors encountered during development and their solutions.

---

## ⚠️ Error 1: Missing Column in Database Table

### 🔴 Error Message
```bash
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) table user has no column named name
[SQL: INSERT INTO user (name, email, password) VALUES (?, ?, ?)]
[parameters: ('string', 'string', 'string')]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
```

### 📝 Cause
This error occurs because the **`user`** table in the SQLite database was created **before adding the `name` column** to the SQLAlchemy model.  
As a result, the **database schema and the model are out of sync**.

### ✅ Solution
Update the database schema so it matches the SQLAlchemy model.

### 🔧 Steps to Fix
1. Generate a new Alembic migration:
   ```bash
   alembic revision --autogenerate -m "add name column to user"
   ```
2. Apply the migration:
   ```bash
   alembic upgrade head
   ```
3. Verify that the `user` table now includes the `name` column.

---

## ⚠️ Error 2: Alembic Migration Driver Issue

### 🔴 Error Message
```bash
sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:driver
```

### 📝 Cause
This error occurs because Alembic could not find the correct database driver in the connection URL.  
In the default `alembic.ini`, the URL is set to a placeholder like:
```ini
sqlalchemy.url = driver://user:pass@localhost/dbname
```
Since `driver` is not a valid SQLAlchemy dialect (e.g., `sqlite`, `postgresql`, `mysql`), Alembic fails to initialize.

### ✅ Solution
Update the `alembic.ini` file with the correct database URL.

### 🔧 Steps to Fix
1. Open `alembic.ini` in your project folder.
2. Replace the placeholder line:
   ```ini
   sqlalchemy.url = driver://user:pass@localhost/dbname
   ```
   with the actual database connection string. For example, if using SQLite:
   ```ini
   sqlalchemy.url = sqlite:///./blog.db
   ```
3. Run the migration commands again:
   ```bash
   alembic revision --autogenerate -m "add name column to user"
   alembic upgrade head
   ```
alembic revision --autogenerate -m "add user_id column to user"
---

## ⚠️ Error 3: call CryptContext 
1 - to call this method from passlib.context
2 - must insatll bcrypt schema ... pip install bcrypt



## ⚠️ Error 4 : Authentication

### 🔴 Error Message
   user = db.query(models.UserModel).filter(models.UserModel.email ==  request.email).first() 
AttributeError: 'OAuth2PasswordRequestForm' object has no attribute 'email'

### 📝 Cause
    user = db.query(models.UserModel).filter(models.UserModel.email ==  request.email).first()
    here i'm make models.UserModel.email ==  request.email

### ✅ Solution


in authentication form the input field name is username not email so we must call it username if than in backend call email 

  user = db.query(models.UserModel).filter(models.UserModel.email ==  request.username ).first()
    here i'm make models.UserModel.email ==  request.email




## ⚠️ Error 4 : get request un Authentication 


def login(request:OAuth2PasswordRequestForm= Depends() ,db:Session= Depends(database.get_db)):
from fastapi.security import **OAuth2PasswordRequestForm**
request:OAuth2PasswordRequestForm= Depends() it is so **important** to get request from form in fastapi docs 
