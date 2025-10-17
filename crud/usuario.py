from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate


def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def criar_usuario(db: Session, usuario: UsuarioCreate):
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