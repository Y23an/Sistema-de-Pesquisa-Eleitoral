from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, status, Query
from modules.resposta.service import RespostaService
from modules.resposta.schemas import CriarRespostaSchema, RespostaSchema

router = APIRouter(prefix="/respostas", tags=["Respostas"])

def get_resposta_service() -> RespostaService:
    return RespostaService()

@router.post("/", response_model=List[RespostaSchema]) 
def criar_resposta_endpoint(dados: CriarRespostaSchema, service: RespostaService = Depends(get_resposta_service)):
    return service.criar_resposta(dados)

@router.get("/", response_model=List[RespostaSchema])
def listar_respostas(entrevistado_id: Optional[int] = None, pergunta_id: Optional[int] = None,alternativa_id: Optional[int] = None, data_resposta: Optional[datetime] = None,
    ativo: Optional[bool] = None, service: RespostaService = Depends(get_resposta_service)):
    return service.listar_respostas(entrevistado_id, pergunta_id, alternativa_id, ativo)

@router.get("/{resposta_id}", response_model=RespostaSchema)
def obter_resposta_por_id(resposta_id: int, service: RespostaService = Depends(get_resposta_service)):
    return service.buscar_por_id(resposta_id)

@router.patch("/{resposta_id}/desativar", response_model=RespostaSchema)
def desativar_resposta(resposta_id: int, service: RespostaService = Depends(get_resposta_service)):
    return service.desativar_resposta(resposta_id)