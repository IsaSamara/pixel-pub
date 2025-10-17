from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.estoque import Estoque
from models.produto import Produto
from schemas.estoque import EstoqueCreate


def listar_estoque(db: Session):
    return db.query(Estoque).all()


def criar_estoque(db: Session, estoque: EstoqueCreate):
    # Verifica se o produto existe
    from sqlalchemy import true

    produto = db.query(Produto).filter(Produto.ativo.is_(true())).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db_estoque = Estoque(
        ProdutoId=estoque.ProdutoId,
        Quantidade=estoque.Quantidade,
        DataAtualizacao=estoque.DataAtualizacao
    )
    db.add(db_estoque)
    db.commit()
    db.refresh(db_estoque)
    return db_estoque