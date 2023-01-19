# Los modelos representan las tablas de la bbdd
# AUTOMATIZAR LA CREACION DE CLASES
# Alembic -> Transforma los modelos en tablas y relaciones de la bbdd
# sqlacodegen -> Transforma las tablas y relaciones en clases

# coding: utf-8
from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, String, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

# Agrupacion de ejercicicos
class Patterns(Base):
    __tablename__ = 'patterns'

    pattern_name = Column(String(255), primary_key=True)

# Ejercicio 
class Exercises(Base):
    __tablename__ = 'exercises'

    exercise_name = Column(String(255), primary_key=True)   
    FK_exercise_pattern = Column(String, ForeignKey('patterns.pattern_name'))

    patterns = relationship('Patterns')
    sessions = relationship('ExercisesSessions', back_populates="exercises")

# Representa un dia de entreno 
class Sessions(Base):
    __tablename__ = 'sessions'

    session_date = Column(Date, primary_key=True)

    exercises = relationship('ExercisesSessions', back_populates="sessions")

# Representa un ejercicio en una sesion
class ExercisesSessions(Base):
    __tablename__ = 'exercises_sessions'

    FK_session_exercise = Column(ForeignKey('exercises.exercise_name'), primary_key=True)
    FK_session_date = Column(ForeignKey('sessions.session_date'), primary_key=True)

    exercises = relationship('Exercises', back_populates="sessions")
    sessions = relationship('Sessions', back_populates="exercises")
    sets = relationship('Sets', back_populates="exercises_sessions")

class Sets(Base):
    __tablename__ = 'sets'
    __table_args__ = (
        ForeignKeyConstraint(['FK_set_session_exercise', 'FK_set_session_date'], ['exercises_sessions.FK_session_exercise', 'exercises_sessions.FK_session_date']),
    )
    set_number = Column(Integer, primary_key=True)
    set_weight = Column(String, nullable=False)
    set_repetitions = Column(String, nullable=False)
    set_rir = Column(String, nullable=False)
    FK_set_session_exercise = Column(String)
    FK_set_session_date = Column(Date)
    
    exercises_sessions = relationship('ExercisesSessions', back_populates="sets")
    sqlite_autoincrement=True