from pydantic import BaseModel


class SQLite(BaseModel):
    class Config:
        from_attributes = True


class Pattern(SQLite):
    pattern_name: str


class SetData(BaseModel):
    exercise_name: str
    weight: int
    repetitions: int
    rir: int


class User(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
