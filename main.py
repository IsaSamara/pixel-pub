from fastapi import FastAPI
from routers import produto

app = FastAPI()

app.include_router(produto.router)
