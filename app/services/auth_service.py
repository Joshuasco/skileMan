#AUTH LOGICS
from sqlmodel import Session, select
from ..db.models.user import User
from ..core.security import verify_password
from ..core.logging import logger


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def authenticate(self, email: str, password: str):
        user = self.db.exec(select(User).where(User.email == email)).first()
        
        if not user:
            logger.warning(f"Failed login attempt: User {email} not found.")
            return None
        
        if not verify_password(password, user.hashed_password):
            logger.warning(f"Failed login attempt: Incorrect password for {email}.")
            return None
            
        logger.info(f"User {email} successfully authenticated.")
        return user