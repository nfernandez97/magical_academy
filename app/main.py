from fastapi import FastAPI
import uvicorn
from app.routers import solicitudes, asignaciones
from app.database import init_db

app = FastAPI()

init_db()

app.include_router(solicitudes.router, prefix="/api", tags=["solicitudes"])
app.include_router(asignaciones.router, prefix="/api", tags=["asignaciones"])

