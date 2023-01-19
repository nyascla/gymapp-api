from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_token_header
from ..sql_app.schemes import SQLite
from ..sql_app.dao import exercisesDao
from ..dependencies import get_db 

router = APIRouter(
    prefix="/api/exercises",
    tags=["exercises"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[SQLite.Exercises])
def get_exercises(db: Session = Depends(get_db)):
    return exercisesDao.get_all_exercises(db)   

@router.get("/patterns", response_model=list[SQLite.Pattern])
def get_pattern(db: Session = Depends(get_db)):
    return exercisesDao.get_all_patterns(db)  

@router.get("/{pattern_name}", response_model=list[SQLite.Exercises])
def get_exercises_pattern(pattern_name: str, db: Session = Depends(get_db)):
    db_exercises = exercisesDao.get_pattern_exercises(db, pattern_name)       
    
    if not db_exercises:
        raise HTTPException(status_code=404, detail="Patron no reconocido")    
    
    return db_exercises