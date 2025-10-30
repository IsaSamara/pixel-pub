from pydantic import BaseModel
from datetime import datetime

class ReservaMesaSchema(BaseModel):
    Id: int
    MesaId: int
    UsuarioId: int
    DataReserva: datetime
    Status: str

    class Config:
        orm_mode = True

class ReservaMesaCreate(BaseModel):
    MesaId: int
    UsuarioId: int
    DataReserva: datetime
    Status: str