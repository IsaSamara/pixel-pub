from http.client import HTTPException
from sqlalchemy.orm import Session
from models.reservaMesa import ReservaMesa, Mesa, Usuario
from schemas.reservaMesa import ReservaMesaCreate
from fastapi import HTTPException


def listar_reservaMesas(db: Session):
    return db.query(ReservaMesa).all()

def criar_reservaMesa(db: Session, reservaMesa: ReservaMesaCreate):
    # Verifica se mesa existe
    mesa = db.query(Mesa).filter(Mesa.Id == reservaMesa.MesaId).first()
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa não encontrada")

    # Verifica se usuário existe
    usuario = db.query(Usuario).filter(Usuario.Id == reservaMesa.UsuarioId).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db_reservaMesa = ReservaMesa(
        MesaId=reservaMesa.MesaId,
        UsuarioId=reservaMesa.UsuarioId,
        DataReserva=reservaMesa.DataReserva,
        Status=reservaMesa.Status
    )
    db.add(db_reservaMesa)
    db.commit()
    db.refresh(db_reservaMesa)
    return db_reservaMesa