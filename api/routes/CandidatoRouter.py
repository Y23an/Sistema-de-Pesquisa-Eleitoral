from typing import Optional
from fastapi import APIRouter, Depends, status
from modules.candidato.shemas import CandidatoSchema, CriarCandidatoSchema, AtualizarCandidatoSchema
from modules.candidato.service import CandidatoService

router = APIRouter(prefix="/candidatos", tags=["Candidatos"])

def get_candidato_service() -> CandidatoService:
    return CandidatoService()

@router.post("/",  response_model=CandidatoSchema,status_code=status.HTTP_201_CREATED)
def criar_candidato(candidato: CriarCandidatoSchema, service: CandidatoService = Depends(get_candidato_service)):
    return service.criar_candidato(candidato)

@router.get("/", response_model=list[CandidatoSchema])
def listar_candidatos(
    nome: Optional[str] = None,
    partido: Optional[str] = None,
    cargo: Optional[str] = None,
    ativo: Optional[bool] = None,
    service: CandidatoService = Depends(get_candidato_service)
):
    return service.listar_candidatos(nome, partido, cargo, ativo)

@router.get("/{candidato_id}", response_model=CandidatoSchema)
def obter_candidato_por_id(
    candidato_id: int,
    service: CandidatoService = Depends(get_candidato_service)
):
    return service.obter_candidato_por_id(candidato_id)

@router.put("/{candidato_id}", response_model=CandidatoSchema)
def atualizar_candidato(
    candidato_id: int,
    candidato: AtualizarCandidatoSchema,
    service: CandidatoService = Depends(get_candidato_service)
):
    return service.atualizar_candidato(candidato_id, candidato)

@router.patch(
    "/{candidato_id}/desativar", 
    status_code=status.HTTP_204_NO_CONTENT
)
def desativar_candidato(
    candidato_id: int,
    service: CandidatoService = Depends(get_candidato_service)
):
    service.desativar_candidato(candidato_id)
    return
