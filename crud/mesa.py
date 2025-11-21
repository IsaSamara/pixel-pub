from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.mesa import Mesa
from schemas.mesa import MesaCreate, MesaUpdate

def listar_mesas(db: Session):
    return db.query(Mesa).all()

def criar_mesa(db: Session, mesa: MesaCreate):
    mesa_existe = db.query(Mesa).filter(Mesa.Numero == mesa.Numero).first()
    if mesa_existe:
        raise HTTPException(status_code=400, detail="Mesa já cadastrada")

    db_mesa = Mesa(
        Numero=mesa.Numero,
        Capacidade=mesa.Capacidade,
        Status=mesa.Status
    )
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa

def atualizar_mesa(db: Session, mesa_id: int, mesa: MesaUpdate):
    db_mesa = db.get(Mesa, mesa_id)

    if not db_mesa:
        raise  HTTPException(status_code=404, detail=f"Mesa de ID {mesa_id} não existe")

    db_mesa.Numero = mesa.Numero
    db_mesa.Capacidade = mesa.Capacidade
    db_mesa.Status = mesa.Status

    db.commit()
    db.refresh(db_mesa)
    return db_mesa

def excluir_mesa(db: Session, mesa_id: int):
    db_mesa = db.get(Mesa, mesa_id)

    if not db_mesa:
        if not db_mesa:
            raise HTTPException(status_code=404, detail=f"Mesa de ID {mesa_id} não existe")

    # Remove do banco
    db.delete(db_mesa)
    db.commit()

    return db_mesa
