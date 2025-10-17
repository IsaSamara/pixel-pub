from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.reservaMesa import ReservaMesaSchema, ReservaMesaCreate
from crud.reservaMesa import listar_reservaMesas, criar_reservaMesa

router = APIRouter(
    prefix="/reservaMesas",
    tags=["ReservaMesa"]
)

@router.get("/", response_model=List[ReservaMesaSchema])
def get_reservaMesas(db: Session = Depends(get_db)):
    return listar_reservaMesas(db)

@router.post("/", response_model=ReservaMesaSchema, status_code=201)
def post_mesa(reservaMesa: ReservaMesaCreate, db: Session = Depends(get_db)):
    return criar_reservaMesa(db, reservaMesa)