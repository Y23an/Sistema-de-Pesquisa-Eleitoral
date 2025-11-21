from modules.entrevistado.schemas import CriarEntrevistadoSchema, AtualizarEntrevistadoSchema
from core.db import DataBase

class EntrevistadoRepository:
    QUERY_CRIAR_ENTREVISTADO = """
    INSERT INTO entrevistado (nome, idade, genero, cidade, ativo)
    VALUES (%s, %s, %s, %s, TRUE)
    RETURNING id, nome, idade, genero, cidade, ativo;
    """

    QUERY_LISTAR_ENTREVISTADOS = """
    SELECT id, nome, idade, genero, cidade, ativo
    FROM entrevistado
    WHERE (%s IS NULL OR nome ILIKE %s)
      AND (%s IS NULL OR idade = %s)
      AND (%s IS NULL OR genero ILIKE %s)
      AND (%s IS NULL OR cidade ILIKE %s)
      AND (%s IS NULL OR ativo = %s)
    ORDER BY id;
    """

    QUERY_BUSCAR_ENTREVISTADO_POR_ID = """
    SELECT id, nome, idade, genero, cidade, ativo
    FROM entrevistado
    WHERE id = %s;
    """

    QUERY_ATUALIZAR_ENTREVISTADO = """
    UPDATE entrevistado
    SET
        nome = COALESCE(%s, nome),
        idade = COALESCE(%s, idade),
        genero = COALESCE(%s, genero),
        cidade = COALESCE(%s, cidade)
    WHERE id = %s
    RETURNING id, nome, idade, genero, cidade, ativo;
    """

    QUERY_DESATIVAR_ENTREVISTADO = """
    UPDATE entrevistado
    SET ativo = FALSE
    WHERE id = %s
    RETURNING id, nome, idade, genero, cidade, ativo;
    """

    def criar(self, entrevistado: CriarEntrevistadoSchema):
        parametros = (entrevistado.nome, entrevistado.idade, entrevistado.genero, entrevistado.cidade)
        db = DataBase()
        return db.execute(self.QUERY_CRIAR_ENTREVISTADO, parametros)

    def listar(self, nome: str | None, idade: int | None, genero: str | None, cidade: str | None, ativo: bool | None):
        nome_like = f"%{nome}%" if nome else None
        genero_like = f"%{genero}%" if genero else None
        cidade_like = f"%{cidade}%" if cidade else None
        parametros = (nome, nome_like, idade, idade, genero, genero_like,cidade, cidade, ativo, ativo)
        
        db = DataBase()
        return db.execute(self.QUERY_LISTAR_ENTREVISTADOS, parametros)
    
    def listar_por_id(self, entrevistado_id: int):
        parametros = (entrevistado_id,)
        db = DataBase()
        return db.execute(self.QUERY_BUSCAR_ENTREVISTADO_POR_ID, parametros, many=False)
    
    def atualizar(self, entrevistado_id: int, entrevistado: AtualizarEntrevistadoSchema):
        parametros = (
            entrevistado.nome, 
            entrevistado.idade, 
            entrevistado.genero, 
            entrevistado.cidade, 
            entrevistado_id
        )
        db = DataBase()
        return db.execute(self.QUERY_ATUALIZAR_ENTREVISTADO, parametros, many=False)

    def desativar(self, entrevistado_id: int):
        parametros = (entrevistado_id,)
        db = DataBase()
        return db.execute(self.QUERY_DESATIVAR_ENTREVISTADO, parametros, many=False)