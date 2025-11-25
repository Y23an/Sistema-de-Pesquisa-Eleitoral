from fastapi import FastAPI
from api.routes import PesquisaRouter
from api.routes import CandidatoRouter
from api.routes import EntrevistadoRouter
from api.routes import PerguntaRouter
from api.routes import AlternativaRouter
from api.routes import RespostaRouter
from fastapi.responses import HTMLResponse

app = FastAPI()
app.include_router(PesquisaRouter.router)
app.include_router(CandidatoRouter.router)
app.include_router(EntrevistadoRouter.router)
app.include_router(PerguntaRouter.router)
app.include_router(AlternativaRouter.router)
app.include_router(RespostaRouter.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}