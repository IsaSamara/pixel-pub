from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.movimentoEstoque import MovimentoEstoqueSchema, MovimentoEstoqueCreate
from crud.movimentoEstoque import listar_movimento_estoque, criar_movimento_estoque

router = APIRouter(
    prefix="/movimentoEstoques",
    tags=["MovimentoEstoques"]
)

@router.get("/", response_model=List[MovimentoEstoqueSchema])
def get_movimento_estoque(db: Session = Depends(get_db)):
    return listar_movimento_estoque(db)

@router.post("/", response_model=MovimentoEstoqueSchema, status_code=201)
def post_movimento_estoque(movimento_estoque: MovimentoEstoqueCreate, db: Session = Depends(get_db)):
    return criar_movimento_estoque(db, movimento_estoque)