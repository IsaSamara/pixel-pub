from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.estoque import EstoqueSchema, EstoqueCreate, EstoqueUpdate
from crud.estoque import listar_estoque, criar_estoque, atualizar_estoque, excluir_estoque

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

@router.put("/{estoque_id}", response_model=EstoqueUpdate, status_code=200)
def put_estoque(estoque_id, estoque: EstoqueUpdate, db: Session = Depends(get_db)):
    return atualizar_estoque(db, estoque_id, estoque)

@router.delete("/{estoque_id}", status_code=204)
def delete_estoque(estoque_id: int, db: Session = Depends(get_db)):
    estoque = excluir_estoque(db, estoque_id)
    if not estoque:
        return None