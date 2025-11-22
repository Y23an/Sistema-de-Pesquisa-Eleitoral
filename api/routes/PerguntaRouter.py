from modules.pergunta.schemas import PerguntaSchema, CriarPerguntaSchema, AtualizarPerguntaSchema
from modules.pergunta.service import PerguntaService
from fastapi import APIRouter, Depends, status
from typing import Optional

router = APIRouter(prefix='/pergunta', tags=['Perguntas'])

def get_pergunta_service() -> PerguntaService:
    return PerguntaService()

@router.post("/", response_model=PerguntaSchema, status_code=status.HTTP_201_CREATED)
def criar_pergunta(pergunta: CriarPerguntaSchema, service: PerguntaService = Depends(get_pergunta_service)):
    return service.criar_pergunta(pergunta)

@router.get("/", response_model=list[PerguntaSchema])
def listar_perguntas(
    texto: Optional[str] = None, 
    tipo: Optional[str] = None, 
    pesquisa_id: Optional[int] = None, 
    ativo: Optional[bool] = None,
    service: PerguntaService = Depends(get_pergunta_service)):
    return service.listar_perguntas(texto, tipo, pesquisa_id, ativo)

@router.get("/{pergunta_id}", response_model=PerguntaSchema)
def obter_pergunta_por_id(pergunta_id: int, service: PerguntaService = Depends(get_pergunta_service)):
    return service.obter_pergunta_por_id(pergunta_id)

@router.put("/{pergunta_id}", response_model=PerguntaSchema)
def atualizar_pergunta(pergunta_id: int, pergunta: AtualizarPerguntaSchema, service: PerguntaService = Depends(get_pergunta_service)):
    return service.atualizar_pergunta(pergunta_id, pergunta)

@router.patch("/{pergunta_id}/desativar", status_code=status.HTTP_204_NO_CONTENT)
def desativar_pergunta(pergunta_id: int, service: PerguntaService = Depends(get_pergunta_service)):
    return service.desativar_pergunta(pergunta_id)
    