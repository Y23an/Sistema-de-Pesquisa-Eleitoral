from fastapi import HTTPException, status
from datetime import date
from modules.pesquisa.repository import PesquisaRepository
from modules.pesquisa import schemas

class PesquisaService:
    def __init__(self):
        self.repository = PesquisaRepository()
    
    def criar_pesquisa(self, pesquisa: schemas.CriarPesquisaSchema):
        if pesquisa.data_fim and (pesquisa.data_fim < pesquisa.data_inicio):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A data_fim não pode ser anterior à data_inicio."
            )
        
        return self.repository.criar(pesquisa)
    
    def listar_pesquisas(self, titulo: str | None, status: str | None, data_inicio: date | None, data_fim: date | None, ativo: bool | None):
        return self.repository.get_listar(titulo, status, data_inicio, data_fim, ativo)
    
    def obter_pesquisa_por_id(self, pesquisa_id: int):
        pesquisa = self.repository.listar_por_id(pesquisa_id)
        
        if not pesquisa:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pesquisa não encontrada."
            )
        
        return pesquisa
    
    def desativar_pesquisa(self, pesquisa_id: int):
        pesquisa_desativada = self.repository.desativar(pesquisa_id)
        
        if not pesquisa_desativada:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pesquisa não encontrada para desativação."
            )
        
        return pesquisa_desativada
    
    def atualizar_pesquisa(self, pesquisa_id: int, pesquisa: schemas.AtualizarPesquisaSchema):
        pesquisa_db = self.repository.listar_por_id(pesquisa_id)
        
        if not pesquisa_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pesquisa não encontrada para atualização."
            )
        
        data_inicio_final = pesquisa.data_inicio if pesquisa.data_inicio is not None else pesquisa_db.data_inicio
        data_fim_final = pesquisa.data_fim if pesquisa.data_fim is not None else pesquisa_db.data_fim

        if data_fim_final and data_inicio_final and (data_fim_final < data_inicio_final):
             raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A data_fim não pode ser anterior à data_inicio."
            )

        return self.repository.atualizar(pesquisa_id, pesquisa)