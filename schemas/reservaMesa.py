from pydantic import BaseModel
from datetime import datetime

class ReservaMesaSchema(BaseModel):
    Id: int
    MesaId: int
    UsuarioId: int
    DataReserva: datetime
    Status: str

    class Config:
        from_attributes = True

class ReservaMesaCreate(BaseModel):
    MesaId: int
    UsuarioId: int
    DataReserva: datetime
    Status: str