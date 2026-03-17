from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    email: str

class UsuarioResponse(UsuarioSchema):
    id: int

    class Config:
        from_attributes = True