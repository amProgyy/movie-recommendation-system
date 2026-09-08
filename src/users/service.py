from sqlalchemy.orm import Session
from passlib.context import CryptContext

from src.users.models import User

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

def hash_pwd(pwd : str) -> str:
    return pwd_context.hash(pwd)

def verify_pwd(plain_pwd : str, hashed_pwd : str) -> bool:
    return pwd_context.verify(plain_pwd, hashed_pwd)

def get_user_by_email(db : Session, email : str):
    return db.query(User).filter(User.email==email).first()

def get_user_by_username(db : Session, username : str):
    return db.query(User).filter(User.username == username).first()

def create_user(db : Session, username : str, email : str, pwd : str):
    hashed_pwd = hash_pwd(pwd)

    user = User(username=username, email=email, password_hash = hashed_pwd)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user