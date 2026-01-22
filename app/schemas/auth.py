from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr

##### DATA VALIDATION #####

# Base model 
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True)

#  Input Model (user input)
class LoginRequest(SQLModel):
    email: EmailStr
    password: str

#  Response Model 
class TokenResponse(SQLModel):
    access_token: str
    token_type: str = "bearer"
    user: UserBase  # Includes only the email, not the password