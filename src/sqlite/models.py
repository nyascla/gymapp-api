import uuid

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.sqlite.database import get_sqlite

# Declaración base para los modelos
Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    name = Column(String(255), primary_key=True)
    password = Column(String(255))

    # Relaciones
    sessions = relationship("Session", back_populates="user_relation")


class Pattern(Base):
    __tablename__ = 'patterns'

    name = Column(String(255), primary_key=True)

    # Relaciones
    exercises = relationship('Exercise', back_populates='pattern_relation')


class Exercise(Base):
    __tablename__ = 'exercises'

    name = Column(String(255), primary_key=True)
    pattern = Column(String, ForeignKey('patterns.name'))

    # Relaciones
    pattern_relation = relationship('Pattern', back_populates='exercises')
    sessions = relationship('ExerciseSession', back_populates='exercise')


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    date = Column(Date)
    user = Column(String, ForeignKey('users.name'))

    # Relaciones
    user_relation = relationship('User', back_populates="sessions")
    exercises = relationship('ExerciseSession', back_populates='session')


class ExerciseSession(Base):
    __tablename__ = 'exercises_sessions'

    # Nuevo ID único para simplificar las relaciones
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String(36), ForeignKey('sessions.id'))
    exercise_name = Column(String(255), ForeignKey('exercises.name'))

    # Relación con los sets
    sets = relationship('Set', back_populates='exercise_session')

    # Relación con Exercise y Session
    exercise = relationship('Exercise', back_populates='sessions')
    session = relationship('Session', back_populates='exercises')


class Set(Base):
    __tablename__ = 'sets'

    id = Column(Integer, primary_key=True, autoincrement=True)  # ID único para la tabla
    exercise_session_id = Column(String(36), ForeignKey('exercises_sessions.id'), nullable=False)
    set_number = Column(Integer)  # Este será el número del set, que se establecerá en el trigger
    repetitions = Column(Integer)
    weight = Column(Integer)
    rir = Column(Integer)

    # Relaciones
    exercise_session = relationship('ExerciseSession', back_populates='sets')


def init_patterns(db):
    patterns = ["Push", "Pull", "Legs"]
    for pattern_name in patterns:
        db_pattern = Pattern(name=pattern_name)
        db.add(db_pattern)
        db.commit()
        db.refresh(db_pattern)


def init_exercises(db):
    exercises = [
        ("Bench Press", "Push"),
        ("Squad", "Legs"),
        ("Pull-Ups", "Pull"),
        ("Shoulder Pres", "Push"),
    ]

    for exercises_name, pattern_name in exercises:
        db_exercises = Exercise(name=exercises_name, pattern=pattern_name)
        db.add(db_exercises)
        db.commit()
        db.refresh(db_exercises)


def init():
    db = next(get_sqlite())

    db_session = db.query(Pattern)
    if not db_session.all():
        init_patterns(db)

    db_session = db.query(Exercise)
    if not db_session.all():
        init_exercises(db)
