from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.produto import Produto
from schemas.produto import ProdutoCreate, ProdutoUpdate


def listar_produtos(db: Session):
    return db.query(Produto).all()

def criar_produto(db: Session, produto: ProdutoCreate):
    db_produto = Produto(
        Nome=produto.Nome,
        Categoria=produto.Categoria,
        DataValidade=produto.DataValidade
    )
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def atualizar_produto(db: Session, produto: ProdutoUpdate, id: int):
    db_produto = db.query(Produto).filter(Produto.Id == id).first()

    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    for nome, valor in produto.model_dump(exclude_unset=True).items():
        setattr(db_produto, nome, valor)

    db.commit()
    db.refresh(db_produto)
    return db_produto