from fastapi import FastAPI
from api.routes import PesquisaRouter

app = FastAPI()
app.include_router(PesquisaRouter.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}