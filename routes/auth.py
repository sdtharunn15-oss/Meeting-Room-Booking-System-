from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.user import User
from schemas.user import UserCreate, Login
from auth.jwt import create_token

from passlib.context import CryptContext


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


pwd = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.username == user.username
    ).first()


    if existing:
        raise HTTPException(
            400,
            "Username already exists"
        )


    new_user = User(
        username=user.username,
        password=pwd.hash(user.password),
        role=user.role
    )


    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return {
        "message":"User registered successfully"
    }




@router.post("/login")
def login(
    data: Login,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == data.username
    ).first()


    if not user:
        raise HTTPException(
            401,
            "Invalid username or password"
        )


    if not pwd.verify(
        data.password,
        user.password
    ):
        raise HTTPException(
            401,
            "Invalid username or password"
        )


    token = create_token(
        {
            "id": user.id,
            "role": user.role
        }
    )


    return {
        "access_token": token,
        "token_type":"bearer"
    }