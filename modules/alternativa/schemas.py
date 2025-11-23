# from pydantic import BaseModel
# from typing import Optional

# class AlternativaSchema(BaseModel):
#     id: int
#     texto: str
#     pergunta_id: int
#     candidato_id: Optional[int] = None
#     ativo: bool
#     class Config:
#         from_attributes = True

# class CriarAlternativaSchema(BaseModel):
#     texto: str
#     pergunta_id: int
#     candidato_id: Optional[int] = None

# class AtualizarAlternativaSchema(BaseModel):
#     texto: str | None = None
#     pergunta_id: int | None = None
#     candidato_id: Optional[int] = None
#     ativo: bool | None = None
from pydantic import BaseModel
from typing import Optional

# --- CORREÇÃO AQUI ---
# Antes: class AlternativaSchema:
# Depois:
class AlternativaSchema(BaseModel): 
    id: int
    texto: str
    pergunta_id: int
    candidato_id: Optional[int]
    ativo: bool
    
    class Config:
        from_attributes = True

class CriarAlternativaSchema(BaseModel):
    texto: str
    pergunta_id: int
    candidato_id: Optional[int] = None

class AtualizarAlternativaSchema(BaseModel):
    texto: str | None = None
    pergunta_id: int | None = None
    candidato_id: Optional[int] = None