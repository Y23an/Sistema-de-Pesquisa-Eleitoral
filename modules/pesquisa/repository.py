from core.db import DataBase
from modules.pesquisa.schemas import CriarPesquisaSchema, PesquisaSchema, AtualizarPesquisaSchema
from datetime import date

class PesquisaRepository:
  QUERY_CRIAR_PESQUISA = """
  INSERT INTO pesquisa (titulo, data_inicio, data_fim, status, ativo)
  VALUES (%s, %s, %s, %s, TRUE)
  RETURNING id, titulo, data_inicio, data_fim, status, ativo;
  """

  QUERY_LISTAR_PESQUISAS = """
  SELECT id, titulo, data_inicio, data_fim, status, ativo
  FROM pesquisa
  WHERE (%s IS NULL OR titulo ILIKE %s) -- <-- ALTERADO AQUI
    AND (%s IS NULL OR status = %s)
    AND (%s IS NULL OR data_inicio >= %s)
    AND (%s IS NULL OR data_fim <= %s)
    AND (%s IS NULL OR ativo = %s)
  ORDER BY id;
  """

  QUERY_BUSCAR_PESQUISA_POR_ID = """
  SELECT id, titulo, data_inicio, data_fim, status, ativo
  FROM pesquisa
  WHERE id = %s;
  """

  QUERY_DESATIVAR_PESQUISA = """
  UPDATE pesquisa
  SET ativo = FALSE
  WHERE id = %s
  RETURNING id, titulo, data_inicio, data_fim, status, ativo;
  """

  QUERY_ATUALIZAR_PESQUISA = """
  UPDATE pesquisa
  SET
    titulo = COALESCE(%s, titulo),
    data_inicio = COALESCE(%s, data_inicio),
    data_fim = COALESCE(%s, data_fim),
    status = COALESCE(%s, status)
  WHERE id = %s
  RETURNING id, titulo, data_inicio, data_fim, status, ativo;
  """

  def criar(self, pesquisa: CriarPesquisaSchema):
    parametros = (pesquisa.titulo, pesquisa.data_inicio, pesquisa.data_fim, pesquisa.status) 
    db = DataBase()
    resultado = db.execute(self.QUERY_CRIAR_PESQUISA, parametros)
    return resultado
  

  def get_listar(self, titulo: str | None, status: str | None, data_inicio: date | None, data_fim: date | None, ativo: bool | None):
      titulo_like = f"%{titulo}%" if titulo is not None else None
      parametros = (
          titulo,
          titulo_like,
          status, status,
          data_inicio, data_inicio,
          data_fim, data_fim,
          ativo, ativo
      )
      
      db = DataBase()
      resultado = db.execute(self.QUERY_LISTAR_PESQUISAS, parametros)
      return resultado
  
  def listar_por_id(self, pesquisa_id: int):
    parametros = (pesquisa_id,)
    db = DataBase()
    resultado = db.execute(self.QUERY_BUSCAR_PESQUISA_POR_ID, parametros, many=False)
    return resultado
  
  def desativar(self, pesquisa_id: int):
    parametros = (pesquisa_id,)
    db = DataBase()
    resultado = db.execute(self.QUERY_DESATIVAR_PESQUISA, parametros, many=False)
    return resultado
  
  def atualizar(self, pesquisa_id: int, pesquisa: AtualizarPesquisaSchema):
    parametros = (pesquisa.titulo, pesquisa.data_inicio, pesquisa.data_fim, pesquisa.status, pesquisa_id)
    db = DataBase()
    resultado = db.execute(self.QUERY_ATUALIZAR_PESQUISA, parametros, many=False)
    return resultado







