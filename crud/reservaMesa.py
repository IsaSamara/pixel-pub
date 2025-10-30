from sqlalchemy.orm import Session
from models.reservaMesa import ReservaMesa
from schemas.reservaMesa import ReservaMesaCreate

def listar_reserva_mesa(db: Session):
    return db.query(ReservaMesa).all()

def criar_reserva_mesa(db: Session, reserva_mesa: ReservaMesaCreate):

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