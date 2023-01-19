from pydantic import BaseModel
import datetime

class SQLite(BaseModel):
    class Config:
        orm_mode = True


class Pattern(SQLite):
    pattern_name: str

class Exercises(SQLite):
    exercise_name: str
    FK_exercise_pattern: str   
    
class Sessions(SQLite):
    session_date: datetime.date
    
class ExercisesSessions(SQLite):
    FK_session_exercise: str
    FK_session_date: datetime.date

class Sets(SQLite):
    set_number: int
    set_weight: str
    set_repetitions: str
    set_rir: str 
    FK_set_session_exercise: str
    FK_set_session_date: datetime.date 
