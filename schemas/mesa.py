from pydantic import BaseModel


class MesaSchema(BaseModel):
    Id: int
    Numero: str
    Capacidade: int
    Status: str

    class Config:
        orm_mode = True

class MesaCreate(BaseModel):
    Numero: str
    Capacidade: int
    Status: str