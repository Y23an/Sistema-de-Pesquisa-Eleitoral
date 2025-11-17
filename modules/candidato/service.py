from fastapi import HTTPException, status
from modules.candidato.repository import CandidatoRepository
from modules.candidato.shemas import CandidatoSchema, CriarCandidatoSchema, AtualizarCandidatoSchema

class CandidatoService:
    def __init__(self):
        self.repository = CandidatoRepository()

    def criar_candidato(self, candidato: CriarCandidatoSchema):
        return self.repository.criar(candidato)

    def listar_candidatos(self, nome: str | None, partido: str | None, cargo: str | None, ativo: bool | None):
        return self.repository.listar(nome, partido, cargo, ativo)

    def obter_candidato_por_id(self, candidato_id: int):
        candidato = self.repository.listar_por_id(candidato_id)
        
        if not candidato:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Candidato não encontrado."
            )
        
        return candidato

    def atualizar_candidato(self, candidato_id: int, candidato_dados: AtualizarCandidatoSchema):
        candidato_existente = self.repository.listar_por_id(candidato_id)
        
        if not candidato_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Candidato não encontrado para atualização."
            )
        return self.repository.atualizar(candidato_id, candidato_dados)

    def desativar_candidato(self, candidato_id: int):
        candidato_desativado = self.repository.desativar(candidato_id)
        
        if not candidato_desativado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Candidato não encontrado para desativação."
            )
        
        return candidato_desativado