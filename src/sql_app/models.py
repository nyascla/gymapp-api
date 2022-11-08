# Los modelos representan las tablas de la bbdd
# AUTOMATIZAR LA CREACION DE CLASES
# Alembic -> Transforma los modelos en tablas y relaciones de la bbdd
# sqlacodegen -> Transforma las tablas y relaciones en clases

from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ETAPA(Base):
    __tablename__ = 'ETAPA'

    id = Column(String(255), primary_key=True)
    fehca_ini = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)


class PATRON(Base):
    __tablename__ = 'PATRON'

    id = Column(String(255), primary_key=True)


class PLANTILLA(Base):
    __tablename__ = 'PLANTILLA'

    id = Column(String(255), primary_key=True)


class EJERCICIO(Base):
    __tablename__ = 'EJERCICIO'

    id = Column(String(255), primary_key=True)
    PATRON_id = Column(ForeignKey('PATRON.id'), nullable=False)

    PATRON = relationship('PATRON')
    PLANTILLAs = relationship('PLANTILLA', secondary='EJERCICIO_PLANTILLA')
    SESION_GYM = relationship('SESIONGYM', secondary='EJERCICIO_REALIZADO')


class SESIONGYM(Base):
    __tablename__ = 'SESION_GYM'

    fecha = Column(Date, primary_key=True)
    ETAPA_id = Column(ForeignKey('ETAPA.id'), nullable=False)
    PLANTILLA_id = Column(ForeignKey('PLANTILLA.id'))

    ETAPA = relationship('ETAPA')
    PLANTILLA = relationship('PLANTILLA')


t_EJERCICIO_PLANTILLA = Table(
    'EJERCICIO_PLANTILLA', metadata,
    Column('EJERCICIO_id', ForeignKey('EJERCICIO.id'), primary_key=True, nullable=False),
    Column('PLANTILLA_id', ForeignKey('PLANTILLA.id'), primary_key=True, nullable=False)
)


t_EJERCICIO_REALIZADO = Table(
    'EJERCICIO_REALIZADO', metadata,
    Column('SESION_GYM_fecha', ForeignKey('SESION_GYM.fecha'), primary_key=True, nullable=False),
    Column('EJERCICIO_id', ForeignKey('EJERCICIO.id'), primary_key=True, nullable=False)
)


class SERIEPLANTILLA(Base):
    __tablename__ = 'SERIE_PLANTILLA'
    __table_args__ = (
        ForeignKeyConstraint(['EJERCICIO_PLANTILLA_EJERCICIO_id', 'EJERCICIO_PLANTILLA_PLANTILLA_id'], ['EJERCICIO_PLANTILLA.EJERCICIO_id', 'EJERCICIO_PLANTILLA.PLANTILLA_id']),
    )

    id = Column(String(255), primary_key=True)
    repeticiones = Column(Integer, nullable=False)
    rir = Column(Integer, nullable=False)
    EJERCICIO_PLANTILLA_EJERCICIO_id = Column(String(255), nullable=False)
    EJERCICIO_PLANTILLA_PLANTILLA_id = Column(String(255), nullable=False)

    EJERCICIO_PLANTILLA_EJERCICIO = relationship('EJERCICIOPLANTILLA')


class SERIEREALIZADA(Base):
    __tablename__ = 'SERIE_REALIZADA'
    __table_args__ = (
        ForeignKeyConstraint(['EJERCICIO_REALIZADO_SESION_GYM_fecha', 'EJERCICIO_REALIZADO_EJERCICIO_id'], ['EJERCICIO_REALIZADO.SESION_GYM_fecha', 'EJERCICIO_REALIZADO.EJERCICIO_id']),
    )

    id = Column(String(255), primary_key=True)
    peso = Column(Integer, nullable=False)
    repeticiones = Column(Integer, nullable=False)
    rir = Column(Integer, nullable=False)
    EJERCICIO_REALIZADO_SESION_GYM_fecha = Column(Date, nullable=False)
    EJERCICIO_REALIZADO_EJERCICIO_id = Column(String(255), nullable=False)

    EJERCICIO_REALIZADO = relationship('EJERCICIOREALIZADO')
