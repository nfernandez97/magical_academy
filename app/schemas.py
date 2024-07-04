from pydantic import BaseModel, Field, constr, conint
from typing import Optional

class SolicitudBase(BaseModel):
    nombre: constr(max_length=20, pattern=r'^[a-zA-Z]+$') # type: ignore
    apellido: constr(max_length=20, pattern=r'^[a-zA-Z]+$') # type: ignore
    identificacion: constr(max_length=20, pattern=r'^[a-zA-Z0-9]+$')  # type: ignore
    edad: conint(gt=0, lt=100)  # type: ignore
    afinidad_magica: constr(pattern=r'^(Oscuridad|Luz|Fuego|Agua|Viento|Tierra)$') # type: ignore

class SolicitudCreate(SolicitudBase):
    pass

class Solicitud(SolicitudBase):
    id: int
    estatus: Optional[str] = Field(default="Pendiente")
    
    class Config:
        orm_mode = True

class Asignacion(BaseModel):
    solicitud_id: Optional[int]
    grimorio: Optional[str]

    class Config:
        orm_mode = True
