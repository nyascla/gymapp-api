from pydantic import BaseModel
from . import SQLite
import datetime

class ChartData(BaseModel):
    labels: list[str]
    data: list[int]

class CreateSet(BaseModel):
    weight: str
    repetitions: str
    rir: str  

class SessionWithSets(BaseModel):
    session_date: datetime.date
    sets: list[SQLite.Sets]
    sets_value: int
