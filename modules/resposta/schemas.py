from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ItemRespostaSchema(BaseModel):
    pergunta_id: int
    alternativa_id: int | None = None
    texto_resposta: str | None = None

class CriarRespostaSchema(BaseModel):
    entrevistado_id: int
    respostas: List[ItemRespostaSchema]

class RespostaSchema(BaseModel):
    id: int | None = None
    entrevistado_id: int
    pergunta_id: int
    alternativa_id: int | None = None
    texto_resposta: str | None = None
    data_resposta: datetime 
    ativo: bool

    class Config:
        from_attributes = True