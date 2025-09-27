from pydantic import BaseModel
from datetime import datetime

class ProdutoSchema(BaseModel):
    Id: int
    Nome: str
    Categoria: str
    DataValidade: datetime

    class Config:
        orm_mode = True

class ProdutoCreate(BaseModel):
    Nome: str
    Categoria: str
    DataValidade: datetime