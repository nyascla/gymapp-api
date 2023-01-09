from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_token_header
from ..sql_app import schemas
from ..sql_app.dao import ejerciciosDao
from ..dependencies import get_db 

router = APIRouter(
    prefix="/api/exercises",
    tags=["ejercicios"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[schemas.Ejercicio])
def get_exercises(db: Session = Depends(get_db)):
    return ejerciciosDao.get_ejercicios(db)   

@router.get("/patterns", response_model=list[schemas.Patron])
def get_pattern(db: Session = Depends(get_db)):
    return ejerciciosDao.get_patrones(db)  

@router.get("/{patron}", response_model=list[schemas.Ejercicio])
def get_exercises_pattern(patron: str, db: Session = Depends(get_db)):
    db_ejercicios = ejerciciosDao.get_ejercicios_patron(db, patron)       
    if not db_ejercicios:
        raise HTTPException(status_code=404, detail="Patron no reconocido")    
    return db_ejercicios