from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_token_header
from ..sql_app.schemes import SQLite, Client
from ..sql_app.dao import sessionsDao
from ..dependencies import get_db 

router = APIRouter(
    prefix="/api/sessions",
    tags=["sessions"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

#
# Crea la session de hoy
#
@router.get("/", response_model=SQLite.Sessions)
def get_session(db: Session = Depends(get_db)):
    db_sesion = sessionsDao.getSesion(db, date.today())   
    
    if db_sesion is None:
        db_sesion = sessionsDao.createSesion(db, date.today()) 

    return db_sesion

#
# Todas las sesiones de un ejercicio
#
@router.get("/{exercise}", response_model=list[Client.SessionWithSets])
def get_sessions_exercise(exercise: str, db: Session = Depends(get_db)):
    return sessionsDao.getSessionsWithSets(db, exercise)

# 
# todas las series de un ejercicio en una sesion
#
@router.get("/{exercise}/{session}", response_model=list[SQLite.Sets])
def get_sets_sessions(exercise: str, session: date, db: Session = Depends(get_db)):
    return sessionsDao.getSets(db, exercise, session)

#
# Anyade una serie al ejercicio, si el ejercicio no existe lo crea
#
@router.post("/{exercise}", response_model=SQLite.Sets)
def add_set(exercise: str, createSet: Client.CreateSet, db: Session = Depends(get_db)):
    db_exercise = sessionsDao.getExerciseSessionToday(db, exercise, date.today())
    
    if db_exercise is None:
        db_exercise = sessionsDao.createExercise(db, exercise, date.today())

    db_sesion = sessionsDao.createSet(db, 
                                        db_exercise.FK_session_exercise, 
                                        db_exercise.FK_session_date, 
                                        createSet)
    
    return db_sesion


#
# Datos del grafico
#
@router.get("/chart/Data/{exercise}", response_model=list[Client.ChartData])
def get_chart_data(exercise: str, db: Session = Depends(get_db)):
    return sessionsDao.getChartData(db, exercise)