from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.estoque import Estoque
from models.produto import Produto
from schemas.estoque import EstoqueCreate, EstoqueUpdate

def listar_estoque(db: Session):
    return db.query(Estoque).all()

def criar_estoque(db: Session, estoque: EstoqueCreate):
    produto_existe = db.query(Produto).filter(Produto.Id == estoque.ProdutoId).first()
    if not produto_existe:
        raise HTTPException(status_code=400, detail="Produto não existe")

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
    db_estoque = db.get(Estoque, estoque_id)

    if not db_estoque:
        raise HTTPException(status_code=404, detail=f"Estoque com ID {estoque_id} não existe")

    db_estoque.Quantidade = estoque.Quantidade
    db_estoque.DataAtualizacao = estoque.DataAtualizacao

    db.commit()
    db.refresh(db_estoque)

    return db_estoque

def excluir_estoque(db: Session, estoque_id: int):
    db_estoque = db.get(Estoque, estoque_id)

    if not db_estoque:
        raise HTTPException(status_code=404, detail=f"Estoque com ID {estoque_id} não existe")

    # Remove do banco
    db.delete(db_estoque)
    db.commit()

    return db_estoque

