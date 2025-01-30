from math import e
from typing import Annotated
from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ValidatorFunctionWrapHandler, ValidationError, WrapValidator

app = FastAPI(title="My fist API")

# USER :
# user_id (UUID),
# username (5 and 10 characters),
# age (>0 and <100),
# email


def valid_username(value: str, handler: ValidatorFunctionWrapHandler) -> str:
    if value != "fernando":
        return handler(value)
    else:
        raise Exception("lol")


class UserCreate(BaseModel):
    username: Annotated[str, Field(
        min_length=5, max_length=10, examples=["johndoe", "alice"]), WrapValidator(valid_username)]
    age: Annotated[int, Field(gt=0, lt=100)]
    email: EmailStr


class User(UserCreate):
    user_id: uuid4
    addresses: list


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/")
def create_user(user: UserCreate):
    return user
