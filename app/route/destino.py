from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.destino import DestinoModel
from app.schemas.destino import DestinoSchema

router = APIRouter(prefix="/destinos", tags=["Destinos"])

@router.post("/")
def criar(dados: DestinoSchema, db: Session = Depends(get_db)):
    destino = DestinoModel(**dados.model_dump())
    db.add(destino)
    db.commit()
    db.refresh(destino)
    return destino

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(DestinoModel).all()