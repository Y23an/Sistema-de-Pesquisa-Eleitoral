from pydantic import BaseModel
from datetime import date
from enum import Enum

class StatusPesquisa(str, Enum):
    ABERTA = "aberta"
    ENCERRADA = "encerrada"

class PesquisaSchema(BaseModel):
    id: int
    titulo: str
    data_inicio: date
    data_fim: date
    status: str 
    ativo: bool

class CriarPesquisaSchema(BaseModel):
    titulo: str
    data_inicio: date
    data_fim: date
    status: str 

class AtualizarPesquisaSchema(BaseModel):
    titulo: str | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    status: StatusPesquisa | None = None
