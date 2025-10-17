from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "Usuario"

    Id = Column(Integer, primary_key=True, index=True)
    Nome = Column(String)
    Cargo = Column(String)
    Email = Column(String)
    Senha = Column(String)