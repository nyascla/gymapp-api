import datetime

from sqlalchemy.orm import Session

from .. import models, schemas



def get_patrones(db: Session):
    return db.query(models.Patron).all()

def get_ejercicios(db: Session):
    return db.query(models.Ejercicio).all()

def get_ejercicios_patron(db: Session, nombre:str):
    return db.query(models.Ejercicio).filter(models.Ejercicio.PATRON_nombre == nombre).all()