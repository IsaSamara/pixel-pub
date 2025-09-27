from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Produto(Base):
    __tablename__ = "Produto"

    Id = Column(Integer, primary_key=True, index=True)
    Nome = Column(String)
    Categoria = Column(String)
    DataValidade = Column(DateTime)