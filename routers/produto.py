from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.produto import ProdutoSchema, ProdutoCreate
from crud.produto import listar_produtos, criar_produto

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