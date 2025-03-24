# TodoApp Mongo

A simple Todo application API built with FastAPI and MongoDB. This project allows users to create, read, update, and delete (CRUD) users and todos, with data stored in a MongoDB database.

## Features
- User management: Create, update, and delete users.
- Todo management: Create, update, delete, and list todos for a specific user.
- MongoDB integration for persistent storage.
- FastAPI for a modern, asynchronous API framework.
- Pydantic for data validation and serialization.

## Prerequisites
- Python 3.8+
- MongoDB (either a local instance or a MongoDB Atlas account)
- `pip` for installing dependencies

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/K-P1/todo-app_mongo.git
cd todoapp_mongo
```

### 2. Install Dependencies
Create a virtual environment and install the required packages:
```bash
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
```

The `requirements.txt` should include:
```
fastapi==0.115.0
pymongo==4.9.1
python-dotenv==1.0.1
uvicorn==0.30.6
```

### 3. Configure MongoDB
1. **Set up MongoDB**:
   - Use MongoDB local MongoDB instance.
   - For a local instance, install MongoDB and ensure it's running on `localhost:27017`.

2. **Set the Connection URI**:
   - Create a `.env` file in the project root:
     ```
     MONGO_DB_CONNECTION_URI=mongodb://localhost:27017
     ```
   - add `<username>`, `<password>`, and `<cluster>` with your MongoDB credentials.

### 4. Run the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. Access the interactive API documentation at `http://localhost:8000/docs`.

## Usage
### Endpoints
- **Users**:
  - `POST /users/`: Create a new user.
  - `GET /users/{user_id}`: Get a user by ID.
  - `PUT /users/{user_id}`: Update a user.
  - `DELETE /users/{user_id}`: Delete a user.
- **Todos**:
  - `POST /todos/`: Create a new todo.
  - `GET /todos/{todo_id}`: Get a todo by ID.
  - `GET /todos/user/{user_id}`: Get all todos for a user.
  - `PUT /todos/{todo_id}`: Update a todo.
  - `DELETE /todos/{todo_id}`: Delete a todo.


## Project Structure
```
todoapp_mongo/
├── .env                # Environment variables (MongoDB URI)
├── database.py         # MongoDB connection setup
├── main.py             # FastAPI application entry point
├── routers/            # API route definitions
│   ├── todo.py
│   ├── user.py
├── schemas/            # Pydantic models for validation
│   ├── __init__.py
│   ├── todo.py
│   ├── user.py
├── serializers/        # Functions to serialize MongoDB documents
│   ├── __init__.py
│   ├── todo.py
│   ├── user.py
├── crud/ 
│   ├── todo.py             # Todo CRUD operations
│   ├── user.py             # User CRUD operations
└── README.md           # Project documentation
```