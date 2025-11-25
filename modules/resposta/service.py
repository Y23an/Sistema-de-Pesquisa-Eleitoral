from typing import List, Optional, Union
from datetime import datetime
from fastapi import HTTPException, status
from modules.resposta.schemas import CriarRespostaSchema, RespostaSchema
from modules.resposta.repository import RespostaRepository

class RespostaService:
    def __init__(self):
        self.repository = RespostaRepository()

    def criar_resposta(self, resposta: CriarRespostaSchema) -> List[RespostaSchema]:
        resultado = self.repository.criar(resposta)
        if isinstance(resultado, str):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=resultado)
        return resultado

    def listar_respostas(self, entrevistado_id: Optional[int] = None, pergunta_id: Optional[int] = None, 
        alternativa_id: Optional[int] = None, data_resposta: Optional[datetime] = None, ativo: Optional[bool] = None) -> List[dict]:
        
        respostas = self.repository.listar(entrevistado_id, pergunta_id, 
            alternativa_id, data_resposta, ativo)
        return respostas

    def buscar_por_id(self, resposta_id: int):
        resposta = self.repository.listar_por_id(resposta_id)
        if not resposta:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Resposta com ID {resposta_id} não encontrada.")
            
        return resposta

    def desativar_resposta(self, resposta_id: int):
        resposta_atualizada = self.repository.desativar(resposta_id)
        if not resposta_atualizada:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foi possível desativar. Resposta ID {resposta_id} não encontrada.")
        return resposta_atualizada
    
