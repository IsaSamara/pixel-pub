from sqlalchemy.orm import Session
from models.mesa import Mesa
from schemas.mesa import MesaCreate


def listar_mesas(db: Session):
    return db.query(Mesa).all()

def criar_mesa(db: Session, mesa: MesaCreate):
    db_mesa = Mesa(
        Numero=mesa.Numero,
        Capacidade=mesa.Capacidade,
        Status=mesa.Status
    )
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa