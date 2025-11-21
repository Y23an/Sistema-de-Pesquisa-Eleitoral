from modules.entrevistado.schemas import CriarEntrevistadoSchema, AtualizarEntrevistadoSchema, EntrevistadoSchema
from modules.entrevistado.service import EntrevistadoService
from typing import Optional
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/entrevistados", tags=["Entrevistados"])

def get_entrevistado_service() -> EntrevistadoService:
    return EntrevistadoService()

@router.post("/", response_model=EntrevistadoSchema, status_code=status.HTTP_201_CREATED)
def criar_entrevistado(entrevistado: CriarEntrevistadoSchema, service: EntrevistadoService = Depends(get_entrevistado_service)):
    return service.criar_entrevistado(entrevistado)

@router.get("/", response_model=list[EntrevistadoSchema])
def listar_entrevistados(
    nome: Optional[str] = None, 
    idade: Optional[int] = None, 
    genero: Optional[str] = None, 
    cidade: Optional[str] = None, 
    ativo: Optional[bool] = None,
    service: EntrevistadoService = Depends(get_entrevistado_service)
):
    return service.listar_entrevistados(nome, idade, genero, cidade, ativo)

@router.get("/{entrevistado_id}", response_model=EntrevistadoSchema)
def obter_entrevistado_por_id(
    entrevistado_id: int,
    service: EntrevistadoService = Depends(get_entrevistado_service)
):
    return service.obter_entrevistado_por_id(entrevistado_id)

@router.put("/{entrevistado_id}", response_model=EntrevistadoSchema)
def atualizar_entrevistado(
    entrevistado_id: int,
    entrevistado: AtualizarEntrevistadoSchema,
    service: EntrevistadoService = Depends(get_entrevistado_service)
):
    return service.atualizar_entrevistado(entrevistado_id, entrevistado)

@router.patch(
    "/{entrevistado_id}/desativar", 
    status_code=status.HTTP_204_NO_CONTENT
)
def desativar_entrevistado(
    entrevistado_id: int,
    service: EntrevistadoService = Depends(get_entrevistado_service)):
    service.desativar_entrevistado(entrevistado_id)
    return
    