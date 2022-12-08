from datetime import date
import random

from sqlalchemy.orm import Session

from .. import models, schemas



def getSesion(db: Session, fecha: date):
    return db.query(models.Sesion).filter(models.Sesion.fecha == fecha).first()

def createSesion(db: Session, fecha: date):
    db_sesion = models.Sesion(fecha=fecha)
    db.add(db_sesion)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion

# Devuelve el ejercicio de la sesion de hoy
def getEjercicioSesion(db: Session, ejercicio: str, fecha: date):
    return db.query(models.EjercicioSesion).filter(
        models.EjercicioSesion.SESION_fecha == fecha).filter(
            models.EjercicioSesion.EJERCICIO_nombre == ejercicio).first()

def createEjercicio(db: Session, ejercicio: str, fecha: date):
    db_sesion = models.EjercicioSesion(EJERCICIO_nombre=ejercicio, SESION_fecha=fecha)
    db.add(db_sesion)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion


def getSerie(db: Session, ejercicio: schemas.EjercicioSesion):
    pass

def createSerie(db: Session, ejercicio: schemas.EjercicioSesion, serie: schemas.SerieCreate):
    db_sesion = models.Serie(**serie.dict(),
                            EJERCICIO_S_nombre=ejercicio.EJERCICIO_nombre,
                            EJERCICIO_S_fecha=ejercicio.SESION_fecha)
    db.add(db_sesion)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion
