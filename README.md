# 🚀 FastAPI Blog & Authentication System

A comprehensive FastAPI application featuring user authentication, blog management, and secure API endpoints with JWT token authentication.

## ✨ Features

- 🔐 **JWT Authentication** - Secure user registration and login
- 📝 **Blog Management** - Create, read, update, delete blog posts
- 👥 **User Management** - User profiles and authentication
- 🗄️ **Database Integration** - SQLAlchemy ORM with Alembic migrations
- 🔒 **OAuth2** - Modern authentication standards
- 🐳 **Docker Ready** - Containerized deployment
- 📊 **Database Schema** - Well-structured database models
- 🛡️ **Security** - Password hashing and secure token handling

## 🏗️ Project Structure

```
FASTAPI/
│── mylearning/                # Extra learning & practice files
│   ├── DeployonDocker/        # Docker deployment experiments
│   ├── sync_async.py          # Async vs Sync exploration
│   └── typeHinting.ipynb      # Python typing experiments
│
│── videoLearning/             # Main project application
│   ├── alembic/               # Alembic migrations
│   ├── blog/                  # Blog application
│   │   ├── repository/        # Business logic layer
│   │   ├── routers/           # API routes (users, blogs, auth)
│   │   ├── database.py        # Database connection setup
│   │   ├── hashing.py         # Password hashing utilities
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── oauth2.py          # OAuth2 authentication & JWT validation
│   │   ├── schema.py          # Pydantic schemas
│   │   ├── tokenJWT.py        # JWT token creation
│   │   └── __init__.py
│   │
│   ├── alembic.ini            # Alembic configuration
│   ├── blog.db                # SQLite database
│   ├── main.py                # FastAPI entry point
│   └── ERRORS.md              # Notes & errors I encountered and solved
│
│── requirements.txt           # Dependencies

```

## 🛠️ Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **JWT** - JSON Web Tokens for authentication
- **OAuth2** - Authorization framework
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI web server
- **Docker** - Containerization platform

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AlaaIsmail2112/fastapi-blog-auth.git
   cd fastapi-blog-auth
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the application**
   ```bash
   uvicorn main:app --reload
   ```

Open API Docs

Swagger UI → `http://127.0.0.1:8000/docs`

ReDoc → `http://127.0.0.1:8000/redoc`

## 📚 API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - User login
- `POST /auth/token` - Get access token

### Users
- `GET /users/` - Get all users
- `GET /users/{id}` - Get user by ID
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

### Blogs
- `GET /blogs/` - Get all blog posts
- `POST /blogs/` - Create new blog post
- `GET /blogs/{id}` - Get blog post by ID
- `PUT /blogs/{id}` - Update blog post
- `DELETE /blogs/{id}` - Delete blog post

## 🔒 Authentication Flow

1. Register a new user or login with existing credentials
2. Receive JWT access token
3. Include token in Authorization header: `Bearer <token>`
4. Access protected endpoints

## 🗄️ Database Schema

The application uses SQLAlchemy models with the following main entities:

- **Users** - User account information
- **Blogs** - Blog post data with user relationships
- **Authentication** - Token and session management

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

## 📝 Environment Variables

Create a `.env` file with the following variables:

```env
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./blog.db
```


## 🙏 Acknowledgments

- FastAPI documentation and community
- SQLAlchemy team for the excellent ORM
- JWT.io for token handling insights

## 📞 About This Learning Journey

This repository represents my hands-on learning experience with FastAPI, following a comprehensive course curriculum. Each commit and module builds upon the previous one, demonstrating progressive skill development in modern Python web development.

**Course Duration**: ~4 hours of practical implementation  
**Learning Style**: Build-while-you-learn approach  
**Focus**: Real-world application development with best practices

---

⭐ **If you're also learning FastAPI, feel free to explore the code and see the progression from basic concepts to a full-featured application!**

📧 **Questions or suggestions?** Feel free to open an issue or reach out!
