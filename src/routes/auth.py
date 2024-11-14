# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.schemes import User, Token
from src.sqlite.dao.sql_dao import SqlDao
from src.sqlite.database import get_sqlite

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=Token)
async def register(user: User, db: Session = Depends(get_sqlite)):
    user_db = SqlDao().get_user(db, user.username)

    if user_db:
        raise HTTPException(status_code=400, detail="Username already registered")

    user_db = SqlDao().post_user(db, user.username, user.password)

    return {"access_token": user_db.name, "token_type": "bearer"}


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_sqlite)):
    auth = SqlDao().check_user(db, form_data.username, form_data.password)

    if not auth:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"access_token": form_data.username, "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    username = token  # Para un sistema básico, el token es el nombre de usuario
    if username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"username": username}
