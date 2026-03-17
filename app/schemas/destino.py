from pydantic import BaseModel

class DestinoSchema(BaseModel):
    nome: str
    pais: str

class DestinoResponse(DestinoSchema):
    id: int

    class Config:
        from_attributes = True