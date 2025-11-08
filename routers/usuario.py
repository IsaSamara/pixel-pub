from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.usuario import UsuarioSchema, UsuarioCreate, UsuarioUpdate
from crud.usuario import listar_usuarios, criar_usuario, atualizar_usuario, excluir_usuario

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

@router.put("/{usuario_id}", response_model=UsuarioUpdate, status_code=200)
def put_usuario(usuario_id, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    return atualizar_usuario(db, usuario_id, usuario)

@router.delete("/{usuario_id}", status_code=200)
def delete_usuario(usuario_id, db: Session = Depends(get_db)):
    usuario = excluir_usuario(db, usuario_id)
    if not usuario:
        return None