# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

users_db: Dict[str, str] = {}

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=User)
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db[user.username] = user.password  # Guardar usuario en memoria
    return user


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": form_data.username, "token_type": "bearer"}


@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    username = token  # Para un sistema básico, el token es el nombre de usuario
    if username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"username": username}