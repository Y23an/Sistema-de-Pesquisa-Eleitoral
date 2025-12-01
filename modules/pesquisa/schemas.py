from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import List

class StatusPesquisa(str, Enum):
    ABERTA = "aberta"
    ENCERRADA = "encerrada"

class PesquisaSchema(BaseModel):
    id: int
    titulo: str
    data_inicio: date
    data_fim: date
    status: StatusPesquisa
    ativo: bool

class CriarPesquisaSchema(BaseModel):
    titulo: str
    data_inicio: date
    data_fim: date
    status: StatusPesquisa

class AtualizarPesquisaSchema(BaseModel):
    titulo: str | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    status: StatusPesquisa | None = None

class AlternativaPublicaSchema(BaseModel):
    id: int
    texto: str
    candidato_id: int | None = None

class PerguntaPublicaSchema(BaseModel):
    id: int
    texto: str
    tipo: str
    alternativas: List[AlternativaPublicaSchema] = []

class QuestionarioSchema(BaseModel):
    pesquisa_id: int
    titulo: str
    perguntas: List[PerguntaPublicaSchema]

class ItemApuracaoSchema(BaseModel):
    candidato: str
    total_votos: int

class ResultadoPesquisaSchema(BaseModel):
    pesquisa_id: int
    apuracao: List[ItemApuracaoSchema]

class StatsPesquisaSchema(BaseModel):
    perguntas: int
    respondentes: int
    respostas: int


