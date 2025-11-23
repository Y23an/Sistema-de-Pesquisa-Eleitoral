from modules.alternativa.repository import AlternativaRepository
from modules.alternativa.schemas import CriarAlternativaSchema, AtualizarAlternativaSchema
from fastapi import HTTPException, status

class AlternativaService:
    def __init__(self):
        self.repository = AlternativaRepository()

    def criar_alternativa(self, alternativa: CriarAlternativaSchema):
        try:
         return self.repository.criar(alternativa)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao criar alternativa: {e}")

    def listar_alternativas(self, texto: str | None, pergunta_id: int | None, candidato_id: int | None, ativo: bool | None):
        return self.repository.listar(texto, pergunta_id, candidato_id, ativo)
    
    def listar_alternativas_por_id(self, id: int):
        entrevistado = self.repository.listar_por_id(id)
        if not entrevistado:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alternativa não encontrada")
        return entrevistado

    def atualizar_alternativa(self, id: int, alternativa: AtualizarAlternativaSchema):
        self.listar_alternativas_por_id(id)
        try:
            return self.repository.atualizar(id, alternativa)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao atualizar alternativa: {e}")

    def desativar_alternativa(self, id: int):
        self.listar_alternativas_por_id(id)
        try:
            return self.repository.desativar(id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro ao deletar alternativa: {e}")
    
    