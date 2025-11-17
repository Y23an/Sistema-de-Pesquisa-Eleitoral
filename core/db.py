import psycopg2
from core import settings
from psycopg2.extras import RealDictCursor

class DataBase:
    def __init__(self):
        self.db_config = {
            "host": settings.DB_HOST,
            "database": settings.DB_NAME,
            "user": settings.DB_USER,
            "password": settings.DB_PASSWORD,
            "port": settings.DB_PORT
        }

    def _get_connection(self):
        return psycopg2.connect(**self.db_config)

    def execute(self, sql: str, params: tuple = None, many: bool = True):
        is_cud = sql.strip().upper().startswith(("INSERT", "UPDATE", "DELETE"))
        result = None

        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(sql, params) 
                    if is_cud:
                        conn.commit()
                        if "RETURNING" in sql.upper():
                            result = cursor.fetchone()
                    else:
                        result = cursor.fetchall() if many else cursor.fetchone()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Erro no banco de dados: {error}")
            raise
            
        return result