
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models.user import User
from app.schemas.base import UserCreate
from app.schemas.user import UserRead, UserLogin, Token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=UserRead, status_code=201)
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = User.register(db, data.model_dump())
        db.commit()
        db.refresh(user)
        return user

    except ValueError as exc:
        db.rollback()
        message = str(exc)
        status = 409 if "already exists" in message else 400
        raise HTTPException(status_code=status, detail=message)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Username or email already exists"
        )


@router.post("/login", response_model=Token)
def login_user(data: UserLogin, db: Session = Depends(get_db)):
    result = User.authenticate(db, data.username, data.password)

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    return result
