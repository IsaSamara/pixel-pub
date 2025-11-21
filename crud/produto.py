from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.produto import Produto
from schemas.produto import ProdutoCreate, ProdutoUpdate

def listar_produtos(db: Session):
    return db.query(Produto).all()

def criar_produto(db: Session, produto: ProdutoCreate):
    produto_existente = db.query(Produto).filter(Produto.Nome == produto.Nome).first()
    if produto_existente:
        raise HTTPException(status_code=400, detail="Produto com este nome já existe.")

    db_produto = Produto(
        Nome=produto.Nome,
        Categoria=produto.Categoria,
        DataValidade=produto.DataValidade
    )
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def atualizar_produto(db: Session, produto_id: int, produto: ProdutoUpdate):
    db_produto = db.get(Produto, produto_id)

    if not db_produto:
        raise HTTPException(status_code=404, detail=f"Produto com ID {produto_id} não encontrado.")

    db_produto.Nome = produto.Nome
    db_produto.Categoria = produto.Categoria
    db_produto.DataValidade = produto.DataValidade

    db.commit()
    db.refresh(db_produto)
    return db_produto

def excluir_produto(db: Session, produto_id: int):
    db_produto = db.get(Produto, produto_id)

    if not db_produto:
        raise HTTPException(status_code=404, detail=f"Produto com ID {produto_id} não encontrado.")

    # Remove do banco
    db.delete(db_produto)
    db.commit()

    return db_produto