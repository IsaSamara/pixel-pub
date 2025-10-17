from pydantic import BaseModel


class UsuarioSchema(BaseModel):
    Id: int
    Nome: str
    Cargo: str
    Email: str
    Senha: str

    class Config:
        orm_mode = True

class UsuarioCreate(BaseModel):
    Nome: str
    Cargo: str
    Email: str
    Senha: str