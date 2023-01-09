from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_token_header
from ..sql_app import schemas
from ..sql_app.dao import sesionesDao
from ..dependencies import get_db 

router = APIRouter(
    prefix="/api/sessions",
    tags=["sesiones"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Sesion de hoy
@router.get("/", response_model=schemas.Sesion)
def get_session(db: Session = Depends(get_db)):
    db_sesion = sesionesDao.getSesion(db, date.today())   
    if db_sesion is None:
        db_sesion = sesionesDao.createSesion(db, date.today()) 

    return db_sesion

# anyade una serie al entreno de hoy
@router.post("/{exercise}", response_model=schemas.Serie)
def add_set(exercise: str, set: schemas.SerieFromClient, db: Session = Depends(get_db)):
    # Recupera el ejercicio de la sesion de hoy
    db_ejercicio_hoy = sesionesDao.getEjercicioSesion(db, exercise, date.today())
    # Si el ejercicio no existe lo crea
    if db_ejercicio_hoy is None:
        db_ejercicio_hoy = sesionesDao.createEjercicio(db, exercise, date.today())
    # Crea una serie para dicho ejercicio
    db_sesion = sesionesDao.createSerie(db, db_ejercicio_hoy, set)
    return db_sesion

# Sesion de hoy
@router.get("/{exercise}", response_model=list[schemas.Serie])
def get_exercise_sessions(exercise: str, db: Session = Depends(get_db)):
    d = sesionesDao.getSessions(db, exercise)   
    return sesionesDao.getSets(db, exercise, d.SESION_fecha)

