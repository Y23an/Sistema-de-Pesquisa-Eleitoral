from fastapi import FastAPI
from api.routes import PesquisaRouter
from api.routes import CandidatoRouter

app = FastAPI()
app.include_router(PesquisaRouter.router)
app.include_router(CandidatoRouter.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}