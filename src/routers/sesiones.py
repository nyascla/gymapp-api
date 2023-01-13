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

@router.get("/chartLabels/{exercise}", response_model=list[str])
def get_chart_labels(exercise: str, db: Session = Depends(get_db)):
    res = []
    db_data = sesionesDao.getChartLabels(db, exercise)
    
    for x in db_data:
        res.append(x.SESION_fecha.strftime("%Y-%m-%d"))
        
    return res

@router.get("/chartData/{exercise}", response_model=list[schemas.Serie])
def get_chart_data(exercise: str, db: Session = Depends(get_db)):
    return sesionesDao.getSets(db, exercise)


# Todas las sesiones donde se ha hecho un ejercicio
@router.get("/{exercise}", response_model=list[schemas.ExerciseWithSets])
def get_exercise_sessions(exercise: str, db: Session = Depends(get_db)):
    db_sessions = sesionesDao.getSessions(db, exercise)  
    db_sessions.sort(key=lambda x: x.SESION_fecha,reverse=True)
    res = []
    for x in db_sessions:
        dic = {}
        dic['exerciseName'] = exercise
        dic['sessionDate'] = x.SESION_fecha.strftime("%Y-%m-%d")
        db_sets = sesionesDao.getSets(db, exercise, x.SESION_fecha)
        db_sets.sort(key=lambda x: x.numero)
        dic['sets'] = db_sets
        res.append(dic)
    
    return res 
    
# todas las series de un ejercicio en una sesion
@router.get("/{exercise}/{session}", response_model=list[schemas.Serie])
def get_exercise_sessions(exercise: str, session: date, db: Session = Depends(get_db)):
    return sesionesDao.getSets(db, exercise, session)


