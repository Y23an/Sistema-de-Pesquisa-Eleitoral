from pydantic import BaseModel
from enum import Enum

class TipoPergunta(str, Enum):
    MULTIPLA_ESCOLHA = "multipla_escolha"
    ABERTA = "aberta"

class CriarPerguntaSchema(BaseModel):
    texto: str
    tipo: TipoPergunta
    pesquisa_id: int

class AtualizarPerguntaSchema(BaseModel):
    texto: str | None = None
    tipo: TipoPergunta | None = None
    pesquisa_id: int | None = None

class PerguntaSchema(BaseModel):
    id: int
    texto: str
    tipo: TipoPergunta
    pesquisa_id: int
    ativo: bool

    class Config:
        from_attributes = True