from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.viagem import ViagemModel
from app.models.usuario import UsuarioModel
from app.models.destino import DestinoModel
from app.schemas.viagem import ViagemSchema

router = APIRouter(prefix="/viagens", tags=["Viagens"])

@router.post("/")
def criar(dados: ViagemSchema, db: Session = Depends(get_db)):
    if not db.query(UsuarioModel).filter(UsuarioModel.id == dados.usuario_id).first():
        raise HTTPException(status_code=404, detail="Usuário não existe")

    if not db.query(DestinoModel).filter(DestinoModel.id == dados.destino_id).first():
        raise HTTPException(status_code=404, detail="Destino não existe")

    viagem = ViagemModel(**dados.model_dump())
    db.add(viagem)
    db.commit()
    db.refresh(viagem)
    return viagem

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(ViagemModel).all()