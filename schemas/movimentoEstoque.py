from pydantic import BaseModel
from datetime import datetime

class MovimentoEstoqueSchema(BaseModel):
    Id: int
    EstoqueId: int
    UsuarioId: int
    TipoMovimento: str
    Quantidade: int
    DataMovimentacao: datetime

    class Config:
        from_attributes = True

class MovimentoEstoqueCreate(BaseModel):
    EstoqueId: int
    UsuarioId: int
    TipoMovimento: str
    Quantidade: int
    DataMovimentacao: datetime