from pydantic import BaseModel

class UserValidation(BaseModel):
    email: str
    password: str