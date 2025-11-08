from pydantic import BaseModel

class MesaSchema(BaseModel):
    Id: int
    Numero: str
    Capacidade: int
    Status: str

    class Config:
        from_attributes = True

class MesaCreate(BaseModel):
    Numero: str
    Capacidade: int
    Status: str

class MesaUpdate(BaseModel):
    Numero: str
    Capacidade: int
    Status: str
