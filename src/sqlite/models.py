from sqlalchemy.ext.declarative import declarative_base

from src.sqlite.database import get_sqlite

# Declaración base para los modelos
Base = declarative_base()
metadata = Base.metadata

from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    name = Column(String(255), primary_key=True)
    password_hash = Column(String(255))
    token = Column(String(255), unique=True)
    expires_at = Column(Date)

    # Relaciones
    sets = relationship("Set", back_populates="user_relation")


class Pattern(Base):
    __tablename__ = 'patterns'

    name = Column(String(255), primary_key=True)

    # Relaciones
    exercises = relationship('Exercise', back_populates='pattern_relation')


class Exercise(Base):
    __tablename__ = 'exercises'

    name = Column(String(255), primary_key=True)
    pattern_name = Column(String(255), ForeignKey('patterns.name'))

    # Relaciones
    pattern_relation = relationship('Pattern', back_populates='exercises')
    sets = relationship('Set', back_populates='exercise_relation')


class Set(Base):
    __tablename__ = 'sets'

    id = Column(Integer, primary_key=True, autoincrement=True)  # ID único para la tabla
    user_name = Column(String(255), ForeignKey('users.name'))
    exercise_name = Column(String(255), ForeignKey('exercises.name'))
    date = Column(Date)

    repetitions = Column(Integer)
    weight = Column(Integer)
    rir = Column(Integer)

    # Relaciones
    user_relation = relationship('User', back_populates="sets")
    exercise_relation = relationship('Exercise', back_populates='sets')