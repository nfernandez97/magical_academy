from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/solicitud", response_model=schemas.Solicitud)
def crear_solicitud(solicitud: schemas.SolicitudCreate, db: Session = Depends(get_db)):
    return crud.create_solicitud(db=db, solicitud=solicitud)

@router.get("/solicitud/{id}", response_model=schemas.Solicitud)
def leer_solicitud(id: int, db: Session = Depends(get_db)):
    db_solicitud = crud.get_solicitud(db, solicitud_id=id)
    if db_solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return db_solicitud

@router.put("/solicitud/{id}", response_model=schemas.Solicitud)
def actualizar_solicitud(id: int, solicitud: schemas.SolicitudCreate, db: Session = Depends(get_db)):
    db_solicitud = crud.update_solicitud(db, solicitud_id=id, solicitud=solicitud)
    if db_solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return db_solicitud

@router.delete("/solicitud/{id}", response_model=schemas.Solicitud)
def eliminar_solicitud(id: int, db: Session = Depends(get_db)):
    db_solicitud = crud.delete_solicitud(db, solicitud_id=id)
    if db_solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return db_solicitud

@router.get("/solicitudes", response_model=List[schemas.Solicitud])
def leer_solicitudes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    solicitudes = crud.get_solicitudes(db, skip=skip, limit=limit)
    return solicitudes

@router.patch("/solicitud/{id}/estatus", response_model=schemas.Asignacion)
def actualizar_estatus_solicitud(id: int, estatus: str, db: Session = Depends(get_db)):
    db_solicitud = crud.get_solicitud(db, solicitud_id=id)
    if db_solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    db_solicitud.estatus = estatus
    db.commit()
    db.refresh(db_solicitud)
    db_solicitud = crud.update_estatus_solicitud(db, solicitud_id=id, estatus=estatus)
    return db_solicitud
