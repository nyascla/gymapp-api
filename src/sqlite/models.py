from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Declaración base para los modelos
Base = declarative_base()
metadata = Base.metadata

# Modelo que representa la agrupación de ejercicios (Patrones)
class Patterns(Base):
    __tablename__ = 'patterns'

    pattern_name = Column(String(255), primary_key=True)  # Nombre del patrón como clave primaria

# Modelo que representa un ejercicio específico
class Exercises(Base):
    __tablename__ = 'exercises'

    exercise_name = Column(String(255), primary_key=True)  # Nombre del ejercicio como clave primaria
    FK_exercise_pattern = Column(String, ForeignKey('patterns.pattern_name'))  # Relación con el patrón

    # Relaciones
    patterns = relationship('Patterns')  # Relación con el patrón de ejercicios
    sessions = relationship('ExercisesSessions', back_populates="exercises")  # Relación con sesiones de ejercicios

# Modelo que representa una sesión (un día de entrenamiento)
class Sessions(Base):
    __tablename__ = 'sessions'

    session_date = Column(Date, primary_key=True)  # Fecha de la sesión como clave primaria

    # Relaciones
    exercises = relationship('ExercisesSessions', back_populates="sessions")  # Relación con ejercicios en sesiones

# Modelo que representa la relación entre un ejercicio y una sesión
class ExercisesSessions(Base):
    __tablename__ = 'exercises_sessions'

    FK_session_exercise = Column(ForeignKey('exercises.exercise_name'), primary_key=True)  # Clave foránea a ejercicios
    FK_session_date = Column(ForeignKey('sessions.session_date'), primary_key=True)  # Clave foránea a sesiones

    # Relaciones
    exercises = relationship('Exercises', back_populates="sessions")  # Relación con el ejercicio
    sessions = relationship('Sessions', back_populates="exercises")  # Relación con la sesión
    sets = relationship('Sets', back_populates="exercises_sessions")  # Relación con las series realizadas

# Modelo que representa una serie de un ejercicio dentro de una sesión
class Sets(Base):
    __tablename__ = 'sets'
    __table_args__ = (
        ForeignKeyConstraint(
            ['FK_set_session_exercise', 'FK_set_session_date'],
            ['exercises_sessions.FK_session_exercise', 'exercises_sessions.FK_session_date']
        ),
    )

    set_number = Column(Integer, primary_key=True)  # Número de la serie como clave primaria
    set_weight = Column(String, nullable=False)  # Peso usado en la serie
    set_repetitions = Column(String, nullable=False)  # Repeticiones realizadas en la serie
    set_rir = Column(String, nullable=False)  # RIR (Repeticiones en reserva)
    FK_set_session_exercise = Column(String)  # Clave foránea al ejercicio de la sesión
    FK_set_session_date = Column(Date)  # Clave foránea a la fecha de la sesión

    # Relaciones
    exercises_sessions = relationship('ExercisesSessions', back_populates="sets")  # Relación con la sesión de ejercicio
    sqlite_autoincrement = True  # Para asegurarse de que la clave primaria se autoincremente en SQLite
