from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import Session, select
from .db.session import engine, create_db_and_tables
from .db.models.user import User
from .core.security import get_password_hash
from .api.v1.auth import router
from .core.logging import logger


##### AUTO CREATE DATABASE TABLE AND TEST USER ON STARTUP #####
@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("🚀 Starting application...")
    # Create tables
    create_db_and_tables()
    
    # Create test user 
    with Session(engine) as session:
        test_email = "admin@gmail.com"
        logger.info("Checking if user exist in database...")
        exists = session.exec(select(User).where(User.email == test_email)).first()
        #creates user if no existing user
        if not exists:
            user = User(
                email=test_email, 
                hashed_password=get_password_hash("password123")
            )
            session.add(user)
            session.commit()
            print(f" Database Created! Login with: {test_email} / password123")
    
    yield 
    logger.info("Cleanup: application Shutting down...")

app = FastAPI(title="skileMan Backend API", lifespan=lifespan)

#register routers
app.include_router(router, prefix="/api/v1")

#base rout
@app.get("/")
def root():
    return {"message": "API is running. Visit /docs for Swagger UI"}

