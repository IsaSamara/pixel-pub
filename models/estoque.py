from sqlalchemy import Column, Integer, ForeignKey, DateTime

from database import Base

class Estoque(Base):
    __tablename__ = "Estoque"

    Id = Column(Integer, primary_key=True, index=True)
    ProdutoId = Column(Integer, ForeignKey("Usuario.Id"), nullable=False)
    Quantidade = Column(Integer)
    DataAtualizacao = Column(DateTime)