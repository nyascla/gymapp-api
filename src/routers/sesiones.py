from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_token_header
from ..sql_app import schemas
from ..sql_app.dao import sesionesDao
from ..dependencies import get_db 

router = APIRouter(
    prefix="/api/sesiones",
    tags=["sesiones"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Sesion de hoy
@router.get("/", response_model=schemas.Sesion)
def get_sesion(db: Session = Depends(get_db)):
    db_sesion = sesionesDao.getSesion(db, date.today())   
    if db_sesion is None:
        db_sesion = sesionesDao.createSesion(db, date.today()) 

    return db_sesion

@router.post("/serie/{ejercicio}", response_model=schemas.Serie)
def create_serie(ejercicio: str, serie: schemas.SerieCreate, db: Session = Depends(get_db)):
    # Recupera el ejercicio de la sesion de hoy
    db_ejercicio_hoy = sesionesDao.getEjercicioSesion(db, ejercicio, date.today())
    if db_ejercicio_hoy is None:
        db_ejercicio_hoy = sesionesDao.createEjercicio(db, ejercicio, date.today())

    db_sesion = sesionesDao.createSerie(db, db_ejercicio_hoy, serie)
    return db_sesion