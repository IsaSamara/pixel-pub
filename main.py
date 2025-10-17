# uvicorn main:app --reload
import webbrowser
from fastapi import FastAPI
from routers import produto, usuario, mesa, reservaMesa, estoque, movimentoEstoque

app = FastAPI()

app.include_router(produto.router)

app.include_router(usuario.router)

app.include_router(mesa.router)

app.include_router(reservaMesa.router)

app.include_router(estoque.router)

app.include_router(movimentoEstoque.router)

import threading
def open_browser():
    webbrowser.open("http://127.0.0.1:8000/docs")

threading.Timer(1.5, open_browser).start()