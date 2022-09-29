import jwt

class Auth:
    
    def __init__(self, jwt_secret, jwt_algo):
        self.jwt_secret = jwt_secret
        self.jwt_algo = jwt_algo

    def encodeToken(self, id):
        return jwt.encode({"user_id": id}, self.jwt_secret, algorithm=self.jwt_algo)

    def decodeToken(self, token):
        try:
            return jwt.decode(token, self.jwt_secret, algorithms=[self.jwt_algo])
        except:
            return None
