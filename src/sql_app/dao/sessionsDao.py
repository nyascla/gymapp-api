from datetime import date
import random

from sqlalchemy.orm import Session

from ..schemes import Client, SQLite

from .. import models

def createSesion(db: Session, date: date):
    db_session = models.Sessions(session_date=date)
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def createExercise(db: Session, exercise: str, date: date):
    db_exercise = models.ExercisesSessions(FK_session_exercise=exercise, 
                                         FK_session_date=date)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def createSet(db: Session, exercise: str, date: date, createSet: Client.CreateSet):
    db_set = models.Sets(set_number = None,
                        set_weight = createSet.weight,
                        set_repetitions = createSet.repetitions,
                        set_rir = createSet.rir,
                        FK_set_session_exercise = exercise,
                        FK_set_session_date = date)
    db.add(db_set)
    db.commit()
    db.refresh(db_set)
    return db_set

def getSesion(db: Session, date: date):
    return db.query(models.Sessions).filter(models.Sessions.session_date == date).first()

def getExerciseSessionToday(db: Session, excercice_name: str, date: date):
    return db.query(models.ExercisesSessions).filter(
        models.ExercisesSessions.FK_session_date == date).filter(
            models.ExercisesSessions.FK_session_exercise == excercice_name).first()

def getExerciseSessions(db: Session, exercise: str):                                                            
    return db.query(models.ExercisesSessions).filter(
        models.ExercisesSessions.FK_session_exercise == exercise).all()

def getSets(db: Session, exercise: str, date: date):
    return db.query(models.Sets).filter(
        models.Sets.FK_set_session_date == date).filter(
            models.Sets.FK_set_session_exercise == exercise).all()

def calculateValueSet(sets: list[SQLite.Sets]):
    value_list = [int(set.set_weight) / (1.0278 - 0.0278 * int(set.set_repetitions)) for set in sets]
    return sum(value_list)/len(value_list)   
    

def getSessionsWithSets(db: Session, exercise: str):                                                            
    db_exercise_sessions = getExerciseSessions(db, exercise)

    res = []
    for session in db_exercise_sessions:
        db_sets = getSets(db, exercise, session.FK_session_date)
        
        dic = {}
        dic['session_date'] = session.FK_session_date        
        dic['sets'] = db_sets
        dic['sets_value'] = calculateValueSet(db_sets)
        res.append(dic)  

    return res             

def getChartData(db: Session, exercise: str):                                                            
    return db.query(models.ExercisesSessions).filter(
        models.ExercisesSessions.FK_session_exercise == exercise).offset(0).limit(5).all()
