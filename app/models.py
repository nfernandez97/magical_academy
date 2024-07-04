from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Solicitud(Base):
    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))
    apellido = Column(String(20))
    identificacion = Column(String(10))
    edad = Column(Integer)
    afinidad_magica = Column(Enum("Oscuridad", "Luz", "Fuego", "Agua", "Viento", "Tierra"))
    estatus = Column(String(20), default="Pendiente")
    asignacion = relationship("Asignacion", back_populates="solicitud", uselist=False)

class Asignacion(Base):
    __tablename__ = "asignaciones"

    id = Column(Integer, primary_key=True, index=True)
    solicitud_id = Column(Integer, ForeignKey("solicitudes.id"))
    grimorio = Column(String(20))
    solicitud = relationship("Solicitud", back_populates="asignacion")
