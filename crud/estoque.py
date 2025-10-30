from sqlalchemy.orm import Session
from models.estoque import Estoque
from schemas.estoque import EstoqueCreate

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

