from core.db import Database
from modules.candidato.shemas import CriarCandidatoSchema, AtualizarCandidatoSchema

class CandidatoRepository:


    QUERY_CRIAR_CANDIDATO = """
    INSERT INTO candidato (nome, partido, cargo, ativo)
    VALUES (%s, %s, %s, TRUE)
    RETURNING id, nome, partido, cargo, ativo;
    """


    QUERY_LISTAR_CANDIDATOS = """
    SELECT id, nome, partido, cargo, ativo
    FROM candidato
    WHERE (%s IS NULL OR nome ILIKE %s)
      AND (%s IS NULL OR partido ILIKE %s)
      AND (%s IS NULL OR cargo ILIKE %s)
      AND (%s IS NULL OR ativo = %s)
    ORDER BY id;
    """

    QUERY_BUSCAR_CANDIDATO_POR_ID = """
    SELECT id, nome, partido, cargo, ativo
    FROM candidato
    WHERE id = %s;
    """

    QUERY_ATUALIZAR_CANDIDATO = """
    UPDATE candidato
    SET
        nome = COALESCE(%s, nome),
        partido = COALESCE(%s, partido),
        cargo = COALESCE(%s, cargo)
    WHERE id = %s
    RETURNING id, nome, partido, cargo, ativo;
    """

    QUERY_DESATIVAR_CANDIDATO = """
    UPDATE candidato
    SET ativo = FALSE
    WHERE id = %s
    RETURNING id, nome, partido, cargo, ativo;
    """

    def criar(self, candidato: CriarCandidatoSchema):
        parametros = (candidato.nome, candidato.partido, candidato.cargo)
        db = Database()
        return db.execute(self.QUERY_CRIAR_CANDIDATO, parametros)

    def listar(self, nome: str | None, partido: str | None, cargo: str | None, ativo: bool | None):
        nome_like = f"%{nome}%" if nome else None
        partido_like = f"%{partido}%" if partido else None
        cargo_like = f"%{cargo}%" if cargo else None
        parametros = (
            nome, nome_like,
            partido, partido_like,
            cargo, cargo_like,
            ativo, ativo
        )
        
        db = Database()
        return db.execute(self.QUERY_LISTAR_CANDIDATOS, parametros)

    def listar_por_id(self, candidato_id: int):
        parametros = (candidato_id,)
        db = Database()
        return db.execute(self.QUERY_BUSCAR_CANDIDATO_POR_ID, parametros, many=False)

    def atualizar(self, candidato_id: int, candidato: AtualizarCandidatoSchema):
        parametros = (
            candidato.nome, 
            candidato.partido, 
            candidato.cargo, 
            candidato_id
        )
        db = Database()
        return db.execute(self.QUERY_ATUALIZAR_CANDIDATO, parametros, many=False)

    def desativar(self, candidato_id: int):
        parametros = (candidato_id,)
        db = Database()
        return db.execute(self.QUERY_DESATIVAR_CANDIDATO, parametros, many=False)