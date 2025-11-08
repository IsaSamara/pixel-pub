from pydantic import BaseModel
from datetime import datetime

class ProdutoSchema(BaseModel):
    Id: int
    Nome: str
    Categoria: str
    DataValidade: datetime

    class Config:
        from_attributes = True

class ProdutoCreate(BaseModel):
    Nome: str
    Categoria: str
    DataValidade: datetime

class ProdutoUpdate(BaseModel):
    Nome: str
    Categoria: str
    DataValidade: datetime