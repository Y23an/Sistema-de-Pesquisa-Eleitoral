from core.db import Database
from modules.alternativa.schemas import CriarAlternativaSchema, AtualizarAlternativaSchema

class AlternativaRepository:
    QUERY_CRIAR_ALTERNATIVA = """
        INSERT INTO alternativa(texto, pergunta_id, candidato_id, ativo)
        VALUES (%s, %s, %s, TRUE)
        RETURNING id, texto, pergunta_id, candidato_id, ativo;
    """
    QUERY_BUSCAR_ALTERNATIVAS = """
        SELECT id, texto, pergunta_id, candidato_id, ativo
        FROM alternativa
        WHERE (%s IS NULL OR texto ILIKE %s)
          AND (%s IS NULL OR pergunta_id = %s)
          AND (%s IS NULL OR candidato_id = %s)
          AND (%s IS NULL OR ativo = %s)
        ORDER BY id;
    """
    QUERY_BUSCAR_POR_ID = """
        SELECT id, texto, pergunta_id, candidato_id, ativo
        FROM alternativa
        WHERE id = %s;
    """

    QUERY_ATUALIZAR_ALTERNATIVA = """
        UPDATE alternativa
        SET
            texto = COALESCE(%s, texto),
            pergunta_id = COALESCE(%s, pergunta_id),
            candidato_id = COALESCE(%s, candidato_id)
        WHERE id = %s
        RETURNING id, texto, pergunta_id, candidato_id, ativo;
    """

    QUERY_DESATIVAR_ALTERNATIVA = """
        UPDATE alternativa
        SET ativo = FALSE
        WHERE id = %s
        RETURNING id, texto, pergunta_id, candidato_id, ativo;  
    """

    def criar(self, alternativa: CriarAlternativaSchema):
        parametros = (alternativa.texto, alternativa.pergunta_id, alternativa.candidato_id)
        db = Database()
        return db.execute(self.QUERY_CRIAR_ALTERNATIVA, parametros)
    
    def listar(self, texto: str | None, pergunta_id: int | None, candidato_id: int | None, ativo: bool | None):
        texto_like = f"%{texto}%" if texto else None
        parametros = (texto, texto_like,
                      pergunta_id, pergunta_id,
                      candidato_id, candidato_id,
                      ativo, ativo)
        db = Database()
        return db.execute(self.QUERY_BUSCAR_ALTERNATIVAS, parametros)

    def listar_por_id(self, alternativa_id: int):
        parametros = (alternativa_id,)
        db = Database()
        return db.execute(self.QUERY_BUSCAR_POR_ID, parametros, many=False)
    
    def atualizar(self, alternativa_id: int, alternativa: AtualizarAlternativaSchema):
        parametros = (
            alternativa.texto,
            alternativa.pergunta_id,
            alternativa.candidato_id,
            alternativa_id
        )
        db = Database()
        return db.execute(self.QUERY_ATUALIZAR_ALTERNATIVA, parametros, many=False)

    def desativar(self, alternativa_id: int):
        parametros = (alternativa_id,)
        db = Database()
        return db.execute(self.QUERY_DESATIVAR_ALTERNATIVA, parametros)
