from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    Id: int
    Nome: str
    Cargo: str
    Email: str
    Senha: str

    class Config:
        from_attributes = True

class UsuarioCreate(BaseModel):
    Nome: str
    Cargo: str
    Email: str
    Senha: str

class UsuarioUpdate(BaseModel):
    Nome: str
    Cargo: str
    Email: str
    Senha: str
