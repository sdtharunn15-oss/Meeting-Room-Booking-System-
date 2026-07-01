from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

from database import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


pwd = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


SECRET_KEY = "secretkey"
ALGORITHM = "HS256"



# ---------------- REGISTER ----------------

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    # remove existing user during testing
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        db.delete(existing_user)
        db.commit()


    hashed_password = pwd.hash(
        user.password[:72]
    )


    new_user = User(
        username=user.username,
        password=hashed_password,
        role=user.role
    )


    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return {
        "message": "User registered successfully"
    }




# ---------------- LOGIN ----------------

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()


    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )


    if not pwd.verify(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )


    token_data = {
        "id": db_user.id,
        "sub": db_user.username,
        "role": db_user.role,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }


    token = jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }