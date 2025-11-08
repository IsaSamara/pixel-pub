from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.mesa import MesaSchema, MesaCreate, MesaUpdate
from crud.mesa import listar_mesas, criar_mesa, atualizar_mesa, excluir_mesa

router = APIRouter(
    prefix="/mesas",
    tags=["Mesas"]
)

@router.get("/", response_model=List[MesaSchema])
def get_mesas(db: Session = Depends(get_db)):
    return listar_mesas(db)

@router.post("/", response_model=MesaSchema, status_code=201)
def post_mesa(mesa: MesaCreate, db: Session = Depends(get_db)):
    return criar_mesa(db, mesa)

@router.put("/{mesa_id}", response_model=MesaUpdate, status_code=200)
def put_mesa(mesa_id, mesa: MesaUpdate, db: Session = Depends(get_db)):
    return atualizar_mesa(db, mesa_id, mesa)

@router.delete("/{mesa_id}", status_code=204)
def delete_mesa(mesa_id: int, db: Session = Depends(get_db)):
    mesa = excluir_mesa(db, mesa_id)
    if not mesa:
        return None