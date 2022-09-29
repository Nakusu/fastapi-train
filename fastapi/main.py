import os
from typing import Union
from fastapi import FastAPI

from passlib.hash import sha256_crypt

from sqlalchemy import select
from sqlmodel import Session

from models.db import get_session, init_db
from models.User import User, UserCreate

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return 1

@app.get("/user")
def getUser():
    return None

@app.get("/user/create")
def createUser():
    session = get_session()

    user = User(email="leopold.lepage@gmail.com", password=sha256_crypt.hash("Test123..//"))
    session.add(user)
    session.commit()

    return user
    