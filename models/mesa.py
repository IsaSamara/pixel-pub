from sqlalchemy import Column, Integer, String
from database import Base

class Mesa(Base):
    __tablename__ = "Mesa"

    Id = Column(Integer, primary_key=True, index=True)
    Numero = Column(String)
    Capacidade = Column(Integer)
    Status = Column(String)