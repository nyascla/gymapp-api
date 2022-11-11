from datetime import date, datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies import get_token_header
from ..sql_app import schemas
from ..sql_app.dao import dao_sesiones
from ..dependencies import get_db 

router = APIRouter(
    prefix="/sesiones",
    tags=["sesiones"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

# Sesion de hoy
@router.get("/",response_model=schemas.SesionGymBase)
def get_user(db: Session = Depends(get_db)):
    db_sesion = dao_sesiones.get_sesion(db, str(date.today()))
    #if db_sesion is None:
    #    db_sesion = dao_sesiones.create_sesion(db, str(date.today()))
    
    return db_sesion

