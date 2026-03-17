from fastapi import FastAPI
from app.database import Base, engine

from app.route import usuario, destino, viagem

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Viagens")

app.include_router(usuario.router)
app.include_router(destino.router)
app.include_router(viagem.router)

@app.get("/")
def home():
    return {"mensagem": "API de Viagens funcionando"}