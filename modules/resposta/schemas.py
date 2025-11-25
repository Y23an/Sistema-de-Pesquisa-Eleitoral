from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RespostaSchema(BaseModel):
    id: int | None = None
    entrevistado_id: int
    pergunta_id: int
    alternativa_id: Optional[int] = None
    texto_resposta: Optional[str] = None
    data_resposta: datetime 
    ativo: bool

class ItemRespostaSchema(BaseModel):
    pergunta_id: int
    alternativa_id: Optional[int] = None
    texto_resposta: Optional[str] = None

class CriarRespostaSchema(BaseModel):
    entrevistado_id: int
    respostas: list[ItemRespostaSchema]
