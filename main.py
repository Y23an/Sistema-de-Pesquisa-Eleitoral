from fastapi import FastAPI
from api.routes import PesquisaRouter
from api.routes import CandidatoRouter
from api.routes import EntrevistadoRouter
from api.routes import PerguntaRouter

app = FastAPI()
app.include_router(PesquisaRouter.router)
app.include_router(CandidatoRouter.router)
app.include_router(EntrevistadoRouter.router)
app.include_router(PerguntaRouter.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}