from http.client import HTTPException
from sqlalchemy.orm import Session
from models.reservaMesa import ReservaMesa
from models.mesa import Mesa
from models.usuario import Usuario
from schemas.reservaMesa import ReservaMesaCreate
from fastapi import HTTPException
from sqlalchemy import true



def listar_reserva_mesa(db: Session):
    return db.query(ReservaMesa).all()

def criar_reserva_mesa(db: Session, reserva_mesa: ReservaMesaCreate):
    # Verifica se mesa existe
    mesa = db.query(Mesa).filter(Mesa.ativo.is_(true())).first()
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa não encontrada")

    # Verifica se usuário existe
    usuario = db.query(Usuario).filter(Usuario.ativo.is_(true())).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db_reserva_mesa = ReservaMesa(
        MesaId=reserva_mesa.MesaId,
        UsuarioId=reserva_mesa.UsuarioId,
        DataReserva=reserva_mesa.DataReserva,
        Status=reserva_mesa.Status
    )
    db.add(db_reserva_mesa)
    db.commit()
    db.refresh(db_reserva_mesa)
    return db_reserva_mesa