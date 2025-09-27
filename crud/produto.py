from sqlalchemy.orm import Session
from models.produto import Produto

def listar_produtos(db: Session):
    return db.query(Produto).all()