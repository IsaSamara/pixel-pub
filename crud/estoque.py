from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from models.estoque import Estoque
from schemas.estoque import EstoqueCreate, EstoqueUpdate

def listar_estoque(db: Session):
    return db.query(Estoque).all()

def criar_estoque(db: Session, estoque: EstoqueCreate):
    db_estoque = Estoque(
        ProdutoId=estoque.ProdutoId,
        Quantidade=estoque.Quantidade,
        DataAtualizacao=estoque.DataAtualizacao
    )
    db.add(db_estoque)
    db.commit()
    db.refresh(db_estoque)
    return db_estoque

def atualizar_estoque(db: Session, estoque_id: int, estoque: EstoqueUpdate):
    db_estoque = db.query(Estoque).filter(Estoque.Id == estoque_id).first()

    if not db_estoque:
        return None

    db_estoque.Quantidade = estoque.Quantidade
    db_estoque.DataAtualizacao = estoque.DataAtualizacao

    db.commit()
    db.refresh(db_estoque)

    return db_estoque

def excluir_estoque(db: Session, estoque_id: int):
    db_estoque = db.get(Estoque, estoque_id)

    if not db_estoque:
        return None

    # Remove do banco
    db.delete(db_estoque)
    db.commit()

    return db_estoque

