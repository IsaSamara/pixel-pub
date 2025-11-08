from sqlalchemy.orm import Session
from models.movimentoEstoque import MovimentoEstoque
from schemas.movimentoEstoque import MovimentoEstoqueCreate

def listar_movimento_estoque(db: Session):
    return db.query(MovimentoEstoque).all()

def criar_movimento_estoque(db: Session, movimento_estoque: MovimentoEstoqueCreate):
    db_movimento_estoque = MovimentoEstoque(
        EstoqueId=movimento_estoque.EstoqueId,
        UsuarioId=movimento_estoque.UsuarioId,
        TipoMovimento=movimento_estoque.TipoMovimento,
        Quantidade=movimento_estoque.Quantidade,
        DataMovimentacao=movimento_estoque.DataMovimentacao
    )
    db.add(db_movimento_estoque)
    db.commit()
    db.refresh(db_movimento_estoque)
    return db_movimento_estoque