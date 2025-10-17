from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.reservaMesa import ReservaMesaSchema, ReservaMesaCreate
from crud.reservaMesa import listar_reserva_mesa, criar_reserva_mesa

router = APIRouter(
    prefix="/reservaMesas",
    tags=["ReservaMesa"]
)

@router.get("/", response_model=List[ReservaMesaSchema])
def get_reservaMesas(db: Session = Depends(get_db)):
    return listar_reserva_mesa(db)

@router.post("/", response_model=ReservaMesaSchema, status_code=201)
def post_mesa(reservaMesa: ReservaMesaCreate, db: Session = Depends(get_db)):
    return criar_reserva_mesa(db, reservaMesa)