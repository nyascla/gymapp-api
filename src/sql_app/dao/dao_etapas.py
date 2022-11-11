import datetime

from sqlalchemy.orm import Session

from .. import models, schemas



def get_etapa(db: Session, etapa_id: str):
    print(etapa_id)
    return db.query(models.ETAPA).filter(models.ETAPA.id == etapa_id).first()

def create_etapa(db: Session, etapa: schemas.EtapaCreate):
    #**etapa.dict()
    db_etapa = models.ETAPA(id=etapa.id, fehca_ini=etapa.fehca_ini, fecha_fin=etapa.fecha_fin)
    db.add(db_etapa)
    db.commit()
    db.refresh(db_etapa)
    return db_etapa
