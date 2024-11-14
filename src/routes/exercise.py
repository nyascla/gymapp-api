from datetime import date
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.sqlite.dao.sql_dao import SqlDao
from src.sqlite.database import get_sqlite
from src import schemes

router = APIRouter(
    prefix="",
    tags=["sessions"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/session", response_model=schemes.Sessions)
def get_session(db: Session = Depends(get_sqlite), token: str = Depends(oauth2_scheme)):
    return SqlDao().post_today_session(db, date.today(), token)


@router.get("/exercises", response_model=list[str])
def get_exercises(db: Session = Depends(get_sqlite)):
    return SqlDao().get_exercises(db)


@router.post("/set", response_model=schemes.Sets)
def add_set(set_data: schemes.SetData, db: Session = Depends(get_sqlite)):
    return SqlDao().post_set(db, set_data)


@router.get("/sets/{exercise}", response_model=list[schemes.SessionWithSets])
def get_sessions_exercise(exercise: str, db: Session = Depends(get_sqlite), token: str = Depends(oauth2_scheme)):
    return SqlDao().get_exercise_sessions(db, exercise, token)

