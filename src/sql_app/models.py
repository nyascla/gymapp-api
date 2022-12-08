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
class Patron(Base):
    __tablename__ = 'patron'

    nombre = Column(String(255), primary_key=True)

# Ejercicio 
class Ejercicio(Base):
    __tablename__ = 'ejercicio'

    nombre = Column(String(255), primary_key=True)
    PATRON_nombre = Column(String, ForeignKey('patron.nombre'))

    patron = relationship('Patron')
    sesiones = relationship('EjercicioSesion', back_populates="ejercicio")

# Representa un dia de entreno 
class Sesion(Base):
    __tablename__ = 'sesion'

    fecha = Column(Date, primary_key=True)

    ejercicios = relationship('EjercicioSesion', back_populates="sesion")

# Representa un ejercicio en una sesion
class EjercicioSesion(Base):
    __tablename__ = 'ejercicio_sesion'

    EJERCICIO_nombre = Column(ForeignKey('ejercicio.nombre'), primary_key=True)
    SESION_fecha = Column(ForeignKey('sesion.fecha'), primary_key=True)

    ejercicio = relationship('Ejercicio', back_populates="sesiones")
    sesion = relationship('Sesion', back_populates="ejercicios")
    series = relationship('Serie', back_populates="ejercicioSesion")

class Serie(Base):
    __tablename__ = 'serie'
    __table_args__ = (
        ForeignKeyConstraint(['EJERCICIO_S_nombre', 'EJERCICIO_S_fecha'], ['ejercicio_sesion.EJERCICIO_nombre', 'ejercicio_sesion.SESION_fecha']),
    )
    numero = Column(Integer, primary_key=True)
    peso = Column(Integer, nullable=False)
    repes = Column(Integer, nullable=False)
    rir = Column(Integer, nullable=False)

    EJERCICIO_S_nombre = Column(String, primary_key=True)
    EJERCICIO_S_fecha = Column(String, primary_key=True)
    
    ejercicioSesion = relationship('EjercicioSesion', back_populates="series")

# class SERIEPLANTILLA(Base):
#     __tablename__ = 'SERIE_PLANTILLA'
#     __table_args__ = (
#         ForeignKeyConstraint(['EJERCICIO_PLANTILLA_EJERCICIO_id', 'EJERCICIO_PLANTILLA_PLANTILLA_id'], ['EJERCICIO_PLANTILLA.EJERCICIO_id', 'EJERCICIO_PLANTILLA.PLANTILLA_id']),
#     )

#     id = Column(String(255), primary_key=True)
#     repeticiones = Column(Integer, nullable=False)
#     rir = Column(Integer, nullable=False)
#     EJERCICIO_PLANTILLA_EJERCICIO_id = Column(String(255), nullable=False)
#     EJERCICIO_PLANTILLA_PLANTILLA_id = Column(String(255), nullable=False)

#     EJERCICIO_PLANTILLA_EJERCICIO = relationship('EJERCICIO', secondary=t_EJERCICIO_PLANTILLA)

# t_EJERCICIO_PLANTILLA = Table(
#     'EJERCICIO_PLANTILLA', metadata,
#     Column('EJERCICIO_id', ForeignKey('EJERCICIO.id'), primary_key=True, nullable=False),
#     Column('PLANTILLA_id', ForeignKey('PLANTILLA.id'), primary_key=True, nullable=False)
# )

# class PLANTILLA(Base):
#     __tablename__ = 'PLANTILLA'

#     id = Column(String(255), primary_key=True)

#     SESIONGYM = relationship("SESIONGYM", back_populates="PLANTILLA")

# class ETAPA(Base):
#     __tablename__ = 'ETAPA'

#     id = Column(String(255), primary_key=True)
#     fehca_ini = Column(Date, nullable=False)
#     fecha_fin = Column(Date, nullable=False)

#     SESIONGYM = relationship("SESIONGYM", back_populates="ETAPA")