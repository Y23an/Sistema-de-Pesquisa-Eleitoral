from fastapi import HTTPException, status
from modules.entrevistado.repository import EntrevistadoRepository
from modules.entrevistado.schemas import CriarEntrevistadoSchema, AtualizarEntrevistadoSchema

class EntrevistadoService:
    def __init__(self):
        self.repository = EntrevistadoRepository()
    
    def criar_entrevistado(self, entrevistado: CriarEntrevistadoSchema):
        try:
            return self.repository.criar(entrevistado)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao criar entrevistado: {e}")

    def listar_entrevistados(self, nome : str | None, idade : int | None, genero : str | None, cidade : str | None, ativo : bool | None):
        return self.repository.listar(nome, idade, genero, cidade, ativo)
    
    def obter_entrevistado_por_id(self, entrevistado_id: int):
        entrevistado = self.repository.listar_por_id(entrevistado_id)
        if not entrevistado:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entrevistado não encontrado")
        return entrevistado

    def atualizar_entrevistado(self, entrevistado_id: int, entrevistado: AtualizarEntrevistadoSchema):
        entrevistado_existente = self.obter_entrevistado_por_id(entrevistado_id)
        try:
            return self.repository.atualizar(entrevistado_id, entrevistado)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao atualizar entrevistado: {e}")

    def desativar_entrevistado(self, entrevistado_id: int):
        entrevistado_existente = self.obter_entrevistado_por_id(entrevistado_id)
        try:
            entrevistado_desativado = self.repository.desativar(entrevistado_id)
            if not entrevistado_desativado:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entrevistado não encontrado para desativar")
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao desativar entrevistado: {e}")