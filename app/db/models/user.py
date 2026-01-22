from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    __table_args__ = {"extend_existing": True} # Prevents Duplicate Definition errors during hot-reloads
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str