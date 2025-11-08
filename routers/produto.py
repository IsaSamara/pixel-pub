from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.produto import ProdutoSchema, ProdutoCreate, ProdutoUpdate
from crud.produto import listar_produtos, criar_produto, atualizar_produto, excluir_produto

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.get("/", response_model=List[ProdutoSchema])
def get_produtos(db: Session = Depends(get_db)):
    return listar_produtos(db)

@router.post("/", response_model=ProdutoSchema, status_code=201)
def post_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return criar_produto(db, produto)

@router.put("/{produto_id}", response_model=ProdutoUpdate, status_code=200)
def put_produto(produto_id: int, produto: ProdutoUpdate, db: Session = Depends(get_db)):
    return atualizar_produto(db, produto_id, produto)

@router.delete("/{produto_id}", status_code=204)
def delete_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = excluir_produto(db, produto_id)
    if not produto:
        return None