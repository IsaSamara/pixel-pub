from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.usuario import UsuarioSchema, UsuarioCreate
from crud.usuario import listar_usuarios, criar_usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/", response_model=List[UsuarioSchema])
def get_usuarios(db: Session = Depends(get_db)):
    return listar_usuarios(db)

@router.post("/", response_model=UsuarioSchema, status_code=201)
def post_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)