from pydantic import BaseModel
import datetime
# Los schema son utilizados por FastAPI para las request y responses

#Patron
class Patron(BaseModel):
    nombre: str

    class Config:
        orm_mode = True


#Ejercicio
class Ejercicio(BaseModel):
    nombre: str
    PATRON_nombre: str   
    
    class Config:
        orm_mode = True

#Patron
class SesionBase(BaseModel):
    pass
    
class Sesion(SesionBase):
    fecha: datetime.date
    
    class Config:
        orm_mode = True

#Patron
class EjercicioSesion(BaseModel):
    EJERCICIO_nombre: str
    SESION_fecha: datetime.date
    
    class Config:
        orm_mode = True

#Patron
class SerieCreate(BaseModel):
    numero: int
    peso: int
    repes: int
    rir: int
    
class Serie(SerieCreate):
    EJERCICIO_S_nombre: str
    EJERCICIO_S_fecha: datetime.date
    
    class Config:
        orm_mode = True