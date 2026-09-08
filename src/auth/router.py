from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.users.schemas import UserCreate, Userresponse
from src.users.service import (create_user, get_user_by_email, get_user_by_username)

router = APIRouter(
    prefix='/auth',
    tags=["Authentication"]
)

