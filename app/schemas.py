from pydantic import BaseModel, Field

class Usuario(BaseModel):
    usuario: str
    senha: str

    class Config:
        orm_mode = True
