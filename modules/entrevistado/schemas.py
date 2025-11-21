from pydantic import BaseModel

class EntrevistadoSchema(BaseModel):
    id: int
    nome: str
    idade: int
    genero: str
    cidade: str
    ativo: bool = True

class CriarEntrevistadoSchema(BaseModel):
    nome: str
    idade: int
    genero: str
    cidade: str

class AtualizarEntrevistadoSchema(BaseModel):
    nome: str | None = None
    idade: int | None = None
    genero: str | None = None
    cidade: str | None = None