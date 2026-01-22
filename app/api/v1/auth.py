from fastapi import APIRouter, HTTPException, status
from ...schemas.auth import LoginRequest, TokenResponse
from ...db.session import SessionDep
from ...services.auth_service import AuthService
from ...core.security import create_access_token

router = APIRouter(tags=["Authentication"])

@router.post(
    "/login", 
    response_model=TokenResponse, 
    status_code=status.HTTP_200_OK
)
def login(payload: LoginRequest, db: SessionDep):
    auth_service = AuthService(db)
    user = auth_service.authenticate(payload.email, payload.password)
    
    if not user:
        # Error handling
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generate JWT  
    token = create_access_token(user.email)
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user  # FastAPI filters this through UserBase via TokenResponse
    }



