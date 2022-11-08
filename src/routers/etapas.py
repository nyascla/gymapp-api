from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_token_header
from ..sql_app import crud, schemas
from ..dependencies import get_db 

router = APIRouter(
    prefix="/etapas",
    tags=["etapas"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_user():
    return {}

@router.get("/{etapa_id}", response_model=schemas.Etapa)
def get_user(etapa_id: str, db: Session = Depends(get_db)):
    db_etapa = crud.get_etapa(db, etapa_id=etapa_id)
    print("fin")
    if db_etapa is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_etapa

@router.post("/", response_model=schemas.Etapa)
def create_user(etapa: schemas.EtapaCreate, db: Session = Depends(get_db)):
    db_etapa = crud.get_etapa(db, etapa_id=etapa.id)
    if db_etapa:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_etapa(etapa=etapa, db=db)

