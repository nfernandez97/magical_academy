from sqlalchemy.orm import Session
from . import models, schemas
from random import choice

grimorios = ["Trébol de 1 hoja", "Trébol de 2 hojas", "Trébol de 3 hojas", "Trébol de 4 hojas"]

def create_solicitud(db: Session, solicitud: schemas.SolicitudCreate):
    db_solicitud = models.Solicitud(**solicitud.dict())
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud

def get_solicitud(db: Session, solicitud_id: int):
    return db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()

def get_solicitudes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Solicitud).offset(skip).limit(limit).all()

def update_solicitud(db: Session, solicitud_id: int, solicitud: schemas.SolicitudCreate):
    db_solicitud = db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()
    if db_solicitud:
        for key, value in solicitud.dict().items():
            setattr(db_solicitud, key, value)
        db.commit()
        db.refresh(db_solicitud)
    return db_solicitud

def delete_solicitud(db: Session, solicitud_id: int):
    db_solicitud = db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()
    if db_solicitud:
        db.delete(db_solicitud)
        db.commit()
    return db_solicitud

def update_estatus_solicitud(db: Session, solicitud_id: int, estatus: str):
    db_solicitud = db.query(models.Solicitud).filter(models.Solicitud.id == solicitud_id).first()
    if db_solicitud:
        db_solicitud.estatus = estatus
        if estatus.lower() == "aprobado":
            grimorio = choice(grimorios)
            db_asignacion = models.Asignacion(solicitud_id=db_solicitud.id, grimorio=grimorio)
            db.add(db_asignacion)
            db.commit()
            db.refresh(db_asignacion)
            return db_asignacion
    db_solicitud = models.Asignacion(solicitud_id = None, grimorio = 'No asignado')
    return db_solicitud

def get_asignaciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Asignacion).filter(models.Asignacion.solicitud_id.isnot(None)).offset(skip).limit(limit).all()
