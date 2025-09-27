from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.produto import ProdutoSchema
from crud.produto import listar_produtos

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.get("/", response_model=List[ProdutoSchema])
def get_produtos(db: Session = Depends(get_db)):
    return listar_produtos(db)