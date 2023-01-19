from sqlalchemy.orm import Session

from .. import models

def get_all_patterns(db: Session):
    return db.query(models.Patterns).all()

def get_all_exercises(db: Session) -> list:
    return db.query(models.Exercises).all()

def get_pattern_exercises(db: Session, pattern_name:str):
    return db.query(models.Exercises).filter(models.Exercises.FK_exercise_pattern == pattern_name).all()
    