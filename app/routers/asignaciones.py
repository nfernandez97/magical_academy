from fastapi import APIRouter, Depends
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

@router.get("/asignaciones", response_model=List[schemas.Asignacion])
def leer_asignaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    asignaciones = crud.get_asignaciones(db, skip=skip, limit=limit)
    return asignaciones
