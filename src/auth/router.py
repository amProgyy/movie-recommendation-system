from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.users.schemas import UserCreate, Userresponse
from src.users.service import (create_user, get_user_by_email, get_user_by_username)

router = APIRouter(
    prefix='/auth',
    tags=["Authentication"]
)

@router.post("/signup", response_model = Userresponse)
def signup(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    existing_email = get_user_by_email(
        db, 
        user_data.email
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            deatil="Email already registered"
        )


    existing_username = get_user_by_username(
        db, 
        user_data.username
    )

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )

    user = create_user(
        db=db,
        username=user_data.username,
        email=user_data.email,
        pwd= user_data.password
    )

    return user