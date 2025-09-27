from sqlalchemy.orm import Session
from models.produto import Produto
from schemas.produto import ProdutoCreate


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