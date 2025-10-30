from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base
from sqlalchemy.orm import relationship
import datetime

class ReservaMesa(Base):
    __tablename__ = "ReservaMesa"

    Id = Column(Integer, primary_key=True, index=True)
    MesaId = Column(Integer, ForeignKey("Mesa.Id"), nullable=False)
    UsuarioId = Column(Integer, ForeignKey("Usuario.Id"), nullable=False)
    DataReserva = Column(DateTime, default=datetime.datetime.now())
    Status = Column(String)

    usuario = relationship("Usuario")
    mesa = relationship("Mesa")

