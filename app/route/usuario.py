from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import UsuarioModel
from app.schemas.usuario import UsuarioSchema

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/")
def criar(dados: UsuarioSchema, db: Session = Depends(get_db)):
    usuario = UsuarioModel(**dados.model_dump())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()