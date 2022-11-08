from pydantic import BaseModel
import datetime
# Los schema son utilizados por FastAPI para las request y responses

#Etapas
class EtapaBase(BaseModel):
    id: str
    fehca_ini: datetime.date
    fecha_fin: datetime.date

    class Config:
        orm_mode = True


class EtapaCreate(EtapaBase):   
    pass

class Etapa(EtapaBase):
    pass

#Sesion
class SesionGymBase(BaseModel):
    fecha: datetime.date
    etapa_id: set
    plantilla_id: str
    
    class Config:
        orm_mode = True

#Plantilla
class PlantillaBase(BaseModel):
    id: str
    
    class Config:
            orm_mode = True

#SeriePlantilla
class SeriePlantillaBase(BaseModel):
    pass

class SerieRealizadaBase(BaseModel):
    pass

#Patron
class PatronBase(BaseModel):
    pass




#Ejercicio
class Ejercicio(BaseModel):
    pass   



