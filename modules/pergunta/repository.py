from modules.pergunta.schemas import PerguntaSchema, CriarPerguntaSchema, AtualizarPerguntaSchema
from core.db import Database

class PerguntaRepository:
    QUERY_CRIAR_PERGUNTA = """
    INSERT INTO pergunta (texto, tipo, pesquisa_id)
    VALUES (%s, %s, %s)
    RETURNING id, texto, tipo, pesquisa_id, ativo;
    """
    QUERY_LISTAR_PERGUNTAS = """    
    SELECT id, texto, tipo, pesquisa_id, ativo 
    FROM pergunta
    WHERE (%s IS NULL OR texto ILIKE %s)
      AND (%s IS NULL OR tipo::text ILIKE %s)
      AND (%s IS NULL OR pesquisa_id = %s)
      AND (%s IS NULL OR ativo = %s)
    ORDER BY id;
    """

    QUERY_BUSCAR_PERGUNTA_POR_ID = """
    SELECT id, texto, tipo, pesquisa_id, ativo
    FROM pergunta
    WHERE id = %s;
    """

    QUERY_ATUALIZAR_PERGUNTA = """
    UPDATE pergunta
    SET
        texto = COALESCE(%s, texto),
        tipo = COALESCE(%s, tipo),
        pesquisa_id = COALESCE(%s, pesquisa_id)
    WHERE id = %s
    RETURNING id, texto, tipo, pesquisa_id, ativo;
    """

    QUERY_DESATIVAR_PERGUNTA = """
    UPDATE pergunta
    SET ativo = FALSE
    WHERE id = %s
    RETURNING id, texto, tipo, pesquisa_id, ativo;
    """

    def criar(self, pergunta: CriarPerguntaSchema):
        parametros = (pergunta.texto, pergunta.tipo.value, pergunta.pesquisa_id)
        db = Database()
        return db.execute(self.QUERY_CRIAR_PERGUNTA, parametros)

    def listar(self, texto :str | None, tipo: str | None, pesquisa_id: int | None, ativo: bool | None):
        texto_like = f"{texto}%" if texto else None
        tipo_like = f"{tipo}%" if tipo else None
        parametros = (
            texto, texto_like,
            tipo, tipo_like,
            pesquisa_id, pesquisa_id,
            ativo, ativo
        )
        db = Database()
        return db.execute(self.QUERY_LISTAR_PERGUNTAS, parametros)



    def listar_por_id(self, pergunta_id: int):
        parametros = (pergunta_id,)
        db = Database()
        return db.execute(self.QUERY_BUSCAR_PERGUNTA_POR_ID, parametros, many=False)

    def atualizar(self, pergunta_id: int, pergunta: AtualizarPerguntaSchema):
        parametros = (
            pergunta.texto, 
            pergunta.tipo.value if pergunta.tipo else None, 
            pergunta.pesquisa_id, 
            pergunta_id
        )
        db = Database()
        return db.execute(self.QUERY_ATUALIZAR_PERGUNTA, parametros, many=False)

    def desativar(self, pergunta_id: int):
        parametros = (pergunta_id,)
        db = Database()
        return db.execute(self.QUERY_DESATIVAR_PERGUNTA, parametros, many=False)
