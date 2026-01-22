import jwt  # This is the pyjwt library
from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
from .config import settings

# 1. Initialize Argon2 (Modern & Highly Secure)
password_hash = PasswordHash.recommended()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Uses Argon2 to verify the password safely."""
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generates an Argon2 hash."""
    return password_hash.hash(password)

def create_access_token(subject: str) -> str:
    """Generates a JWT using pyjwt."""
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {
        "exp": expire, 
        "sub": str(subject),
        "iat": datetime.now(timezone.utc) # Good practice: Issued At time
    }
    
    # pyjwt's syntax is slightly different: it returns a string by default
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt



# from datetime import datetime, timedelta, timezone
# from typing import Any, Union
# from jose import jwt
# from passlib.context import CryptContext
# from app.core.config import settings

# # Setup the hashing context
# # bcrypt is the industry standard for password storage
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     """
#     Checks if the plain text password matches the stored hash.
#     The library handles the salt internally.
#     """
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password: str) -> str:
#     """
#     Generates a secure hash from a plain text password.
#     Used during user registration.
#     """
#     return pwd_context.hash(password)

# def create_access_token(subject: Union[str, Any]) -> str:
#     """
#     Generates a JWT for authenticated users.
#     """
#     expire = datetime.now(timezone.utc) + timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
#     )
#     to_encode = {"exp": expire, "sub": str(subject)}
#     encoded_jwt = jwt.encode(
#         to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
#     )
#     return encoded_jwt







# from datetime import datetime, timedelta, timezone
# from jose import jwt
# from app.core.config import settings

# def create_access_token(data: dict):
#     to_encode = data.copy()
#     # Always set an expiration!
#     expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
    
#     # Sign the token with your Secret Key
#     encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
#     return encoded_jwt