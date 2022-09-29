import jwt
from passlib.hash import sha256_crypt
from sqlmodel import select
from models.db import get_session, init_db
from models.User import User, UserCreate

class Auth:
    
    def __init__(self, jwt_secret, jwt_algo):
        self.jwt_secret = jwt_secret
        self.jwt_algo = jwt_algo
        self.session = get_session()

    def encodeToken(self, id):
        return jwt.encode({"user_id": id}, self.jwt_secret, algorithm=self.jwt_algo)

    def findUserById(self, id):
        self.session = get_session()
        statement = select(User).where(User.id == id)
        results = self.session.exec(statement)

        return results.first()

    def verifyEmail(self, email):
        self.session = get_session()
        statement = select(User).where(User.email == email)
        results = self.session.exec(statement)
    
        return True if results.first() != None else False

    def verifyUser(self, email, password):
        self.session = get_session()
        statement = select(User).where(User.email == email)
        results = self.session.exec(statement)

        user = results.first()

        if sha256_crypt.verify(password, user.password):
            return user
        return None

    def getUserByToken(self, token):
        user_id = self.decodeToken(token)
        if user_id == None:
            return None
        user_id = user_id["user_id"]
        return self.findUserById(user_id)

    def decodeToken(self, token):
        try:
            return jwt.decode(token, self.jwt_secret, algorithms=[self.jwt_algo])
        except:
            return None
