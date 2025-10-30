from pydantic import BaseModel
from datetime import datetime


class EstoqueSchema(BaseModel):
    Id: int
    ProdutoId: int
    Quantidade: int
    DataAtualizacao: datetime

    class Config:
        orm_mode = True

class EstoqueCreate(BaseModel):
    ProdutoId: int
    Quantidade: int
    DataAtualizacao: datetime

