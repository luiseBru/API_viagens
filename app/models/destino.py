from sqlalchemy import Column, Integer, String
from app.database import Base

class DestinoModel(Base):
    __tablename__ = "destinos"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    pais = Column(String)