# main.py
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from passlib.context import CryptContext
from database import create_tables, get_user_by_id, get_user_by_email, create_user, update_user, delete_user, get_all_user
from typing import List

app = FastAPI()

# Create database tables
# create_tables() #if no db uncomment this line

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    name: str
    email: str
    greeting_phrase: str
    password: str

class UserInDB(User):
    id: int

@app.post("/users", response_model=UserInDB)
async def create_new_user(user: User):
    # Check if the user with this email already exists
    if get_user_by_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Hash the user's password
    hashed_password = pwd_context.hash(user.password)
    user_data = user.dict()
    user_data['password'] = hashed_password

    # Create the user in the database
    user_id = create_user(user_data)
    return UserInDB(**user_data, id=user_id)

@app.get("/allusers", response_model=List[UserInDB])
async def get_all_users():
    users_db = get_all_user()
    # Return the list of users (you would typically fetch this from a database)
    return users_db

@app.get("/users/{user_id}", response_model=UserInDB)
async def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserInDB(**dict(zip(["id", "name", "email", "greeting_phrase", "password"], user)))


@app.put("/users/{user_id}", response_model=UserInDB)
async def update_user_data(user_id: int, user: User):
    existing_user = get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Update user data
    update_user(user_id, user.model_dump())
    user = get_user_by_id(user_id)
    # Return updated user data
    return UserInDB(**dict(zip(["id", "name", "email", "greeting_phrase", "password"], existing_user)))


@app.delete("/users/{user_id}", response_model=dict)
async def delete_user_data(user_id: int):
    existing_user = get_user_by_id(user_id)
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Delete the user
    delete_user(user_id)

    return {"message": "User deleted successfully"}
