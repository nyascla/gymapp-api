import datetime

from sqlalchemy.orm import Session

from .. import models, schemas



def get_sesion(db: Session, sesion_id: str):
    return db.query(models.SESIONGYM).filter(models.SESIONGYM.fecha == sesion_id).first()

def create_sesion(db: Session, sesion_id: str):
    db_sesion = models.SESIONGYM(fecha=sesion_id, ETAPA_id="ppp", PLANTILLA_id="1")
    db.add(db_sesion)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion
