from core.db import Database
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
    WHERE (%s IS NULL OR titulo ILIKE %s)
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

    QUERY_GET_QUESTIONARIO = """
    SELECT id, titulo FROM pesquisa WHERE id = %s;
    """

    QUERY_GET_PERGUNTAS_PESQUISA = """
    SELECT id, texto, tipo FROM pergunta WHERE pesquisa_id = %s ORDER BY id;
    """

    QUERY_GET_ALTERNATIVAS_PERGUNTA = """
    SELECT id, texto, candidato_id FROM alternativa WHERE pergunta_id = %s ORDER BY id;
    """

    QUERY_APURACAO = """
    SELECT c.nome, COUNT(r.id) as total_votos
    FROM resposta r
    JOIN alternativa a ON r.alternativa_id = a.id
    JOIN candidato c ON a.candidato_id = c.id
    JOIN pergunta p ON a.pergunta_id = p.id
    WHERE p.pesquisa_id = %s AND r.ativo = TRUE
    GROUP BY c.nome
    ORDER BY total_votos DESC;
    """

    QUERY_NUM_PERGUNTAS = "SELECT COUNT(*) as total FROM pergunta WHERE pesquisa_id = %s;"

    QUERY_NUM_RESPOSTAS = """
    SELECT COUNT(r.id) as total FROM resposta r
    JOIN pergunta p ON r.pergunta_id = p.id
    WHERE p.pesquisa_id = %s AND r.ativo = TRUE;
    """

    QUERY_NUM_RESPONDENTES = """
    SELECT COUNT(DISTINCT r.entrevistado_id) as total FROM resposta r
    JOIN pergunta p ON r.pergunta_id = p.id
    WHERE p.pesquisa_id = %s AND r.ativo = TRUE;
    """

    def criar(self, pesquisa: CriarPesquisaSchema):
        parametros = (pesquisa.titulo, pesquisa.data_inicio, pesquisa.data_fim, pesquisa.status) 
        db = Database()
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
        
        db = Database()
        resultado = db.execute(self.QUERY_LISTAR_PESQUISAS, parametros)
        return resultado
  
    def listar_por_id(self, pesquisa_id: int):
        parametros = (pesquisa_id,)
        db = Database()
        resultado = db.execute(self.QUERY_BUSCAR_PESQUISA_POR_ID, parametros, many=False)
        return resultado
  
    def desativar(self, pesquisa_id: int):
        parametros = (pesquisa_id,)
        db = Database()
        resultado = db.execute(self.QUERY_DESATIVAR_PESQUISA, parametros, many=False)
        return resultado
  
    def atualizar(self, pesquisa_id: int, pesquisa: AtualizarPesquisaSchema):
        parametros = (pesquisa.titulo, pesquisa.data_inicio, pesquisa.data_fim, pesquisa.status, pesquisa_id)
        db = Database()
        resultado = db.execute(self.QUERY_ATUALIZAR_PESQUISA, parametros, many=False)
        return resultado


    def get_questionario_completo(self, pesquisa_id: int):
        db = Database()
        pesquisa = db.execute(self.QUERY_GET_QUESTIONARIO, (pesquisa_id,), many=False)
        
        if not pesquisa:
            return None
        
        perguntas_db = db.execute(self.QUERY_GET_PERGUNTAS_PESQUISA, (pesquisa_id,))

        lista_perguntas = []
        for p in perguntas_db:
            p_id = p['id'] 
            
            alternativas_db = db.execute(self.QUERY_GET_ALTERNATIVAS_PERGUNTA, (p_id,))
            alternativas_fmt = []
            
            for alt in alternativas_db:
                alternativas_fmt.append({
                    "id": alt['id'],
                    "texto": alt['texto'],
                    "candidato_id": alt['candidato_id']
                })

            lista_perguntas.append({
                "id": p['id'],
                "texto": p['texto'],
                "tipo": p['tipo'],
                "alternativas": alternativas_fmt
            })
            
        return {
            "pesquisa_id": pesquisa['id'],
            "titulo": pesquisa['titulo'],
            "perguntas": lista_perguntas
        }
    
    def get_apuracao(self, pesquisa_id: int):
        db = Database()
        resultados = db.execute(self.QUERY_APURACAO, (pesquisa_id,))
      
        apuracao_formatada = []
        for result in resultados:
            apuracao_formatada.append({
                "candidato": result['nome'], 
                "total_votos": result['total_votos']
            })
            
        return {
            "pesquisa_id": pesquisa_id,
            "apuracao": apuracao_formatada
        }
    
    def get_estatisticas(self, pesquisa_id: int):
        db = Database()
        
        res_perguntas = db.execute(self.QUERY_NUM_PERGUNTAS, (pesquisa_id,), many=False)
        qtd_perguntas = res_perguntas['total'] if res_perguntas else 0

        res_respostas = db.execute(self.QUERY_NUM_RESPOSTAS, (pesquisa_id,), many=False)
        qtd_respostas = res_respostas['total'] if res_respostas else 0

        res_respondentes = db.execute(self.QUERY_NUM_RESPONDENTES, (pesquisa_id,), many=False)
        qtd_respondentes = res_respondentes['total'] if res_respondentes else 0

        return {
            "perguntas": qtd_perguntas,
            "respondentes": qtd_respondentes,
            "respostas": qtd_respostas
        }
