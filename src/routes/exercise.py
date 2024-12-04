from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src import schemes
from src.sqlite.dao import sql_dao_sets
from src.sqlite.database import get_sqlite

router = APIRouter(
    prefix="",
    tags=["sessions"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/exercises", response_model=list[str])
def get_exercises(db: Session = Depends(get_sqlite)):
    return sql_dao_sets.get_exercises(db)


@router.post("/set", response_model=None)
def add_set(
        set_data: schemes.SetData,
        db: Session = Depends(get_sqlite),
        token: str = Depends(oauth2_scheme)
):
    result = sql_dao_sets.post_set(db, set_data, token)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return result


@router.get("/home_info", response_model=None)
def get_exercises(
        db: Session = Depends(get_sqlite),
        token: str = Depends(oauth2_scheme)
):
    result = sql_dao_sets.home_info(db, token)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return result
