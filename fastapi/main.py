import os
from typing import Union
from fastapi import FastAPI

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
