import datetime

from pydantic import BaseModel


class SQLite(BaseModel):
    class Config:
        orm_mode = True


class Pattern(SQLite):
    pattern_name: str


class Exercises(SQLite):
    exercise_name: str
    FK_exercise_pattern: str


class ExercisesNames(SQLite):
    exercise_name: str


class Sessions(SQLite):
    id: str
    date: datetime.date
    user: str


class ExercisesSessions(SQLite):
    FK_session_exercise: str
    FK_session_date: datetime.date


class Sets(SQLite):
    id: int
    exercise_session_id: str
    set_number: int
    repetitions: int
    weight: int
    rir: int


class ChartData(BaseModel):
    labels: list[str]
    data: list[int]


class SetData(BaseModel):
    session_id: str
    exercise_name: str
    weight: str
    repetitions: str
    rir: str


class SessionWithSets(BaseModel):
    session: datetime.date
    sets: list[Sets]


class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
