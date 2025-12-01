from pydantic import BaseModel
from typing import Optional

class AlternativaSchema(BaseModel): 
    id: int
    texto: str
    pergunta_id: int
    candidato_id: int | None = None
    ativo: bool
    
    class Config:
        from_attributes = True

class CriarAlternativaSchema(BaseModel):
    texto: str
    pergunta_id: int
    candidato_id: int | None = None

class AtualizarAlternativaSchema(BaseModel):
    texto: str | None = None
    pergunta_id: int | None = None
    candidato_id: int | None = None