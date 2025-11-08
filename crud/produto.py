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

def atualizar_produto(db: Session, produto_id: int, produto: ProdutoUpdate):
    db_produto = db.query(Produto).filter(Produto.Id == produto_id).first()

    if not db_produto:
        return None

    db_produto.Nome = produto.Nome
    db_produto.Categoria = produto.Categoria
    db_produto.DataValidade = produto.DataValidade

    db.commit()
    db.refresh(db_produto)
    return db_produto

def excluir_produto(db: Session, produto_id: int):
    db_produto = db.get(Produto, produto_id)

    if not db_produto:
        return None

    # Remove do banco
    db.delete(db_produto)
    db.commit()

    return db_produto