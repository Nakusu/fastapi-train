import os
from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Header, Cookie
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from validation import UserValidation

from starlette.responses import RedirectResponse, Response

from passlib.hash import sha256_crypt

from sqlmodel import Session

from models.db import get_session, init_db
from models.User import User

from auth import Auth

app = FastAPI()
Auth = Auth("fastapiTrain", "HS256")


origins = [
    "http://fastapi.local",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    return {"Hello world!"}

@app.get("/user")
def getUser(response: Response, Authorization: str = Cookie(None)):
    user = Auth.getUserByToken(Authorization)
    if user == None:
        return HTTPException(status_code=401, detail="You are connected, you cannot register another user!")

    return {"id": user.id, "email": user.email}

@app.get("/user/logout")
def logoutUser(response: Response, Authorization: str = Cookie(None)):
    user = Auth.getUserByToken(Authorization)
    if user == None:
        return HTTPException(status_code=401, detail="You are connected!")

    response.delete_cookie("Authorization", path="/", domain="api.fastapi.local")
    return {"You has been logout!"}

@app.post("/user/login")
def loginUser(response: Response, datas: UserValidation):
    user = Auth.verifyUser(datas.email, datas.password)

    if user != None:
        token = Auth.encodeToken(user.id)
        response.set_cookie(
            "Authorization",
            value=token,
            domain="api.fastapi.local",
            httponly=True,
            samesite="Lax",
            secure=False,
        )
        return {"Welcome back!"}

    return {"Bad pass!"}
    

@app.post("/user/register")
def createUser(response: Response, datas: UserValidation = None, session: Session = Depends(get_session), Authorization: str = Cookie(None)):
    token = Auth.decodeToken(Authorization)
    if token != None:
        return HTTPException(status_code=401, detail="You are connected, you cannot register another user!")

    if Auth.verifyEmail(datas.email) == True:
        return "This email is already taken!"

    user = User(email=datas.email, password=sha256_crypt.hash(datas.password))
    session.add(user)
    session.commit()
    session.refresh(user)

    token = Auth.encodeToken(user.id)
    response.set_cookie(
        "Authorization",
        value=token,
        domain="api.fastapi.local",
        httponly=True,
        samesite="Lax",
        secure=False,
        max_age=1800,
        expires=1800,
    )
    return {"You has been register!"}
    