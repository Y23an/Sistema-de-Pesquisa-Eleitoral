from pydantic import BaseModel

class CandidatoSchema(BaseModel):
    id: int
    nome: str
    partido: str
    cargo: str
    ativo: bool
    class Config:
        from_attributes = True

class CriarCandidatoSchema(BaseModel):
    nome: str
    partido: str
    cargo: str

class AtualizarCandidatoSchema(BaseModel):
    nome: str | None = None
    partido: str | None = None
    cargo: str | None = None