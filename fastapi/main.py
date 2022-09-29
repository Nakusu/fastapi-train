import os
from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Header, Cookie
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from starlette.responses import RedirectResponse, Response

from passlib.hash import sha256_crypt

from sqlalchemy import select
from sqlmodel import Session

from models.db import get_session, init_db
from models.User import User, UserCreate

import jwt

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

JWT_SECRET = "fastapiTrain"
JWT_ALGORITHM = "HS256"

def decodeJWT(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return 1

@app.get("/user")
def getUser(Authorization: str = Cookie(None)):
    return decodeJWT(Authorization)

@app.get("/user/create")
def createUser(session: Session = Depends(get_session)):
    user = User(email="leopold.lepage@gmail.com", password=sha256_crypt.hash("Test123..//"))
    session.add(user)
    session.commit()
    session.refresh(user)

    token = jwt.encode({"user_id": user.id}, JWT_SECRET, algorithm=JWT_ALGORITHM)
    response = RedirectResponse(url="/user")
    response.set_cookie(
        "Authorization",
        value=token,
        domain="localhost",
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response
    