from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.estoque import Estoque
from models.usuario import Usuario
from models.movimentoEstoque import MovimentoEstoque
from schemas.movimentoEstoque import MovimentoEstoqueCreate


def listar_movimento_estoque(db: Session):
    return db.query(MovimentoEstoque).all()


def criar_movimento_estoque(db: Session, movimento_estoque: MovimentoEstoqueCreate):
    # Verifica se o Estoque existe
    from sqlalchemy import true

    estoque = db.query(Estoque).filter(Estoque.ativo.is_(true())).first()
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")

    # Verifica se o Usuario existe
    usuario = db.query(Usuario).filter(Usuario.ativo.is_(true())).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    db_movimento_estoque = MovimentoEstoque(
        EstoqueId=movimento_estoque.EstoqueID,
        UsuarioID=movimento_estoque.UsuarioID,
        TipoMovimento=movimento_estoque.TipoMovimento,
        Quantidade=movimento_estoque.Quantidade,
        DataMovimentacao=movimento_estoque.DataMovimentacao
    )
    db.add(db_movimento_estoque)
    db.commit()
    db.refresh(db_movimento_estoque)
    return db_movimento_estoque