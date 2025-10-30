from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.mesa import Mesa
from schemas.mesa import MesaCreate, MesaUpdate


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

def atualizar_mesa(db: Session, mesa: MesaUpdate, id: int):
    db_mesa = db.query(Mesa).filter(Mesa.Id == id).first()

    if db_mesa is None:
        raise HTTPException(status_code=404, detail="Mesa não encontrada")

    for nome, valor in mesa.model_dump(exclude_unset=True).items():
        setattr(db_mesa, nome, valor)

    db.commit()
    db.refresh(db_mesa)
    return db_mesa
