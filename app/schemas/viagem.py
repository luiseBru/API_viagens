from pydantic import BaseModel

class ViagemSchema(BaseModel):
    descricao: str
    usuario_id: int
    destino_id: int

class ViagemResponse(ViagemSchema):
    id: int

    class Config:
        from_attributes = True