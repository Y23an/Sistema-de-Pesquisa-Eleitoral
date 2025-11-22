from fastapi import HTTPException, status
from modules.pergunta.schemas import CriarPerguntaSchema, AtualizarPerguntaSchema
from modules.pergunta.repository import PerguntaRepository

class PerguntaService:
    def __init__(self):
        self.repository = PerguntaRepository()

    def criar_pergunta(self, pergunta: CriarPerguntaSchema):
        nova_pergunta = self.repository.criar(pergunta)
        if nova_pergunta is None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe uma pergunta com este texto."
            )
        return nova_pergunta
    
    def listar_perguntas(self, texto: str | None, tipo: str | None, pesquisa_id: int | None, ativo: bool | None):
        return self.repository.listar(texto, tipo, pesquisa_id, ativo)
    
    def obter_pergunta_por_id(self, id: int):
        pergunta = self.repository.listar_por_id(id)
        if pergunta is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pergunta não encontrada")
        return pergunta

    def atualizar_pergunta(self, id: int, pergunta: AtualizarPerguntaSchema):
        pergunta_atualizada = self.repository.atualizar(id, pergunta)
        if pergunta_atualizada is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pergunta não encontrada para atualizar")
        return pergunta_atualizada

    def desativar_pergunta(self, id: int):
        pergunta_desativada = self.repository.desativar(id)
        if pergunta_desativada is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pergunta não encontrada para desativar")
        return pergunta_desativada
    
