from datetime import datetime
from sqlmodel import SQLModel, Field

class UseBase(SQLModel):
    email: str
    password: str

class User(UseBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)


class UserCreate(UseBase):
    pass