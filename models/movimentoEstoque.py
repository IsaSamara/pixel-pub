from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base
from sqlalchemy.orm import relationship
import datetime
class MovimentoEstoque(Base):
    __tablename__ = "MovimentoEstoque"

    Id = Column(Integer, primary_key=True, index=True)
    EstoqueId = Column(Integer, ForeignKey("Estoque.Id"), nullable=False)
    UsuarioId = Column(Integer, ForeignKey("Usuario.Id"), nullable=False)
    TipoMovimento = Column(String)
    Quantidade = Column(Integer)
    DataMovimentacao = Column(DateTime, default=datetime.datetime.now())

    estoque = relationship("Estoque")
    usuario = relationship("Usuario")

