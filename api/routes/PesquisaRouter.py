from typing import Optional
from fastapi import APIRouter, Depends, status
from modules.pesquisa import schemas
from modules.pesquisa.service import PesquisaService
from modules.pesquisa.schemas import CriarPesquisaSchema, AtualizarPesquisaSchema
from datetime import date

router = APIRouter(prefix="/pesquisas", tags=["Pesquisas"])

def get_pesquisa_service() -> PesquisaService:
    return PesquisaService()

@router.post("/", response_model=schemas.PesquisaSchema, status_code=status.HTTP_201_CREATED)
def criar_pesquisa(pesquisa: CriarPesquisaSchema, service: PesquisaService = Depends(get_pesquisa_service)):
    return service.criar_pesquisa(pesquisa)

@router.get("/", response_model=list[schemas.PesquisaSchema])
def listar_pesquisas(titulo: Optional[str] = None, status: Optional[str] = None, data_inicio: Optional[date] = None,
    data_fim: Optional[date] = None, ativo: Optional[bool] = None, service: PesquisaService = Depends(get_pesquisa_service)):
    return service.listar_pesquisas(titulo, status, data_inicio, data_fim, ativo)

@router.get("/{pesquisa_id}", response_model=schemas.PesquisaSchema)
def obter_pesquisa_por_id(pesquisa_id: int, service: PesquisaService = Depends(get_pesquisa_service)):
    return service.obter_pesquisa_por_id(pesquisa_id)

@router.put("/{pesquisa_id}", response_model=schemas.PesquisaSchema)
def atualizar_pesquisa(pesquisa_id: int, pesquisa: schemas.AtualizarPesquisaSchema, service: PesquisaService = Depends(get_pesquisa_service)):
    return service.atualizar_pesquisa(pesquisa_id, pesquisa)

@router.patch("/{pesquisa_id}/desativar", status_code=status.HTTP_204_NO_CONTENT)
def desativar_pesquisa(pesquisa_id: int, service: PesquisaService = Depends(get_pesquisa_service)):
    service.desativar_pesquisa(pesquisa_id)
    return