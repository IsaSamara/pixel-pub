from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.estoque import EstoqueSchema, EstoqueCreate
from crud.estoque import listar_estoque, criar_estoque

router = APIRouter(
    prefix="/estoques",
    tags=["Estoques"]
)

@router.get("/", response_model=List[EstoqueSchema])
def get_estoque(db: Session = Depends(get_db)):
    return listar_estoque(db)

@router.post("/", response_model=EstoqueSchema, status_code=201)
def post_estoque(estoque: EstoqueCreate, db: Session = Depends(get_db)):
    return criar_estoque(db, estoque)
