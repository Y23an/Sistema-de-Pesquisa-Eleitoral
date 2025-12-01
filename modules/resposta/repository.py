from modules.resposta.schemas import CriarRespostaSchema
from core.db import Database
from datetime import datetime
from sqlite3 import IntegrityError
from typing import List, Union

class RespostaRepository:
    QUERY_CRIAR_RESPOSTA = """
    INSERT INTO resposta (entrevistado_id, pergunta_id, alternativa_id, texto_resposta, data_resposta, ativo) 
    VALUES (%s, %s, %s, %s, %s, TRUE)
    RETURNING id, entrevistado_id, pergunta_id, alternativa_id, texto_resposta, data_resposta, ativo;
    """

    QUERY_LISTAR_RESPOSTAS = """
    SELECT id, entrevistado_id, pergunta_id, alternativa_id, texto_resposta, data_resposta, ativo
    FROM resposta
    WHERE 
        (%s IS NULL OR entrevistado_id = %s)
        AND (%s IS NULL OR pergunta_id = %s)
        AND (%s IS NULL OR alternativa_id = %s)
        AND (%s IS NULL OR data_resposta >= %s)
        AND (%s IS NULL OR ativo = %s)
    ORDER BY id;
    """

    QUERY_LISTAR_RESPOSTAS_POR_ID = """
    SELECT id, entrevistado_id, pergunta_id, alternativa_id, texto_resposta, data_resposta, ativo
    FROM resposta
    WHERE id = %s;
    """

    QUERY_DESATIVAR_RESPOSTA = """
    UPDATE resposta
    SET ativo = FALSE
    WHERE id = %s
    RETURNING id, entrevistado_id, pergunta_id, alternativa_id, texto_resposta, data_resposta, ativo;
    """

    def criar(self, dados: CriarRespostaSchema) -> Union[List[dict], str]:
        db = Database()
        data_agora = datetime.now()
        
        lista_para_inserir = []
        for item in dados.respostas:
            lista_para_inserir.append((
                dados.entrevistado_id,
                item.pergunta_id,
                item.alternativa_id,
                item.texto_resposta,
                data_agora
            ))

        try:
            respostas_com_id = [] 

            for param in lista_para_inserir:
                resultado = db.execute(self.QUERY_CRIAR_RESPOSTA, param, many=False)
                respostas_com_id.append(resultado)

            return respostas_com_id

        except IntegrityError as e:
            erro_msg = str(e).lower()
            
            if "entrevistado" in erro_msg:
                return f"Erro: O Entrevistado com id {dados.entrevistado_id} não existe."
            
            if "pergunta" in erro_msg:
                return "Erro: Uma das perguntas informadas não existe."
                
            if "alternativa" in erro_msg:
                return "Erro: Uma das alternativas informadas não existe."

            return f"Erro de integridade no banco de dados: {e}"
            
        except Exception as e:
            return f"Erro interno inesperado: {e}"
        
        
    def listar(self, entrevistado_id: int | None = None, pergunta_id: int | None = None, 
               alternativa_id: int | None = None, data_inicio: datetime | None = None, ativo: bool | None = None):
        parametros = (
            entrevistado_id, entrevistado_id,
            pergunta_id, pergunta_id,
            alternativa_id, alternativa_id,
            data_inicio, data_inicio,
            ativo, ativo
        )
        db = Database()
        return db.execute(self.QUERY_LISTAR_RESPOSTAS, parametros)  

    def listar_por_id(self, resposta_id: int):
        parametros = (resposta_id,)
        db = Database()
        return db.execute(self.QUERY_LISTAR_RESPOSTAS_POR_ID, parametros, many=False)

    def desativar(self, resposta_id: int):
        parametros = (resposta_id,)
        db = Database()
        return db.execute(self.QUERY_DESATIVAR_RESPOSTA, parametros, many=False)
    


    
    


        
        