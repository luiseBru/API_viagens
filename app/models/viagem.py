from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class ViagemModel(Base):
    __tablename__ = "viagens"

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    destino_id = Column(Integer, ForeignKey("destinos.id"))