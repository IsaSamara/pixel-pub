from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate, UsuarioUpdate

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def criar_usuario(db: Session, usuario: UsuarioCreate):
    usuario_existe = db.query(Usuario).filter(Usuario.Email == usuario.Email).first()
    if usuario_existe:
        raise HTTPException(status_code=400, detail="Este email já está cadastrado")
    db_usuario = Usuario(
        Nome=usuario.Nome,
        Cargo=usuario.Cargo,
        Email=usuario.Email,
        Senha=usuario.Senha
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def atualizar_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = db.get(Usuario, usuario_id)

    if not db_usuario:
        raise HTTPException(status_code=404, detail=f"Usuário com ID {usuario_id} não cadastrado")

    db_usuario.Nome = usuario.Nome
    db_usuario.Cargo = usuario.Cargo
    db_usuario.Email = usuario.Email
    db_usuario.Senha = usuario.Senha


    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def excluir_usuario(db: Session, usuario_id: int):
    db_usuario = db.get(Usuario, usuario_id)

    if not db_usuario:
        raise HTTPException(status_code=404, detail=f"Usuário com ID {usuario_id} não cadastrado")

    db.delete(db_usuario)
    db.commit()

    return db_usuario