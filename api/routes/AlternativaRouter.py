from fastapi import APIRouter, status, Depends
from modules.alternativa.schemas import AlternativaSchema, CriarAlternativaSchema, AtualizarAlternativaSchema
from modules.alternativa.service import AlternativaService
from typing import Optional

router = APIRouter(prefix="/alternativas", tags=["Alternativas"])

def get_alternativa_service() -> AlternativaService:
    return AlternativaService()

@router.post("/", response_model=AlternativaSchema, status_code=status.HTTP_201_CREATED)
def criar_alternativa(
    alternativa: CriarAlternativaSchema, 
    service: AlternativaService = Depends(get_alternativa_service) ):
    return service.criar_alternativa(alternativa)

@router.get("/", response_model=list[AlternativaSchema])
def listar_alternativas(
    texto: Optional[str] = None,
    pergunta_id: Optional[int] = None,
    candidato_id: Optional[int] = None,
    ativo: Optional[bool] = None,
    service: AlternativaService = Depends(get_alternativa_service)):
    return service.listar_alternativas(texto, pergunta_id, candidato_id, ativo)

@router.get("/{alternativa_id}", response_model=AlternativaSchema)
def obter_alternativa_por_id(
    alternativa_id: int, 
    service: AlternativaService = Depends(get_alternativa_service)):
    return service.listar_alternativas_por_id(alternativa_id)

@router.put("/{alternativa_id}", response_model=AlternativaSchema)
def atualizar_alternativa(
    alternativa_id: int, 
    alternativa: AtualizarAlternativaSchema, 
    service : AlternativaService = Depends(get_alternativa_service)):
    return service.atualizar_alternativa(alternativa_id, alternativa)


@router.patch("/{alternativa_id}/desativar", status_code=status.HTTP_204_NO_CONTENT)
def desativar_alternativa(
    alternativa_id: int, 
    service : AlternativaService = Depends(get_alternativa_service)):
    service.desativar_alternativa(alternativa_id)
    return 



