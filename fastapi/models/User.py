from datetime import datetime
from sqlmodel import SQLModel, Field, UniqueConstraint, select

class UseBase(SQLModel):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

class User(UseBase, table=True):
    __tablename__ = "user"

    email: str
    password: str

class UserCreate(UseBase):
    pass