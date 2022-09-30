from pydantic import BaseModel, ValidationError, validator

class UserValidation(BaseModel):
    email: str
    password: str

    @validator("email")
    def validateEmail(cls, v):
        if v is not None and "@" in v and "." in v:
            return v
        raise ValidationError("This is not an email!")

    @validator("password")
    def validatePassword(cls, v):
        if v is not None and len(v) > 3:
            return v
        raise ValidationError("Your password is too short!")
