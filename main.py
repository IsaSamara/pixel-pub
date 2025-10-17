# uvicorn main:app --reload
import webbrowser
from fastapi import FastAPI
from routers import produto

app = FastAPI()

app.include_router(produto.router)

import threading
def open_browser():
    webbrowser.open("http://127.0.0.1:8000/docs")

threading.Timer(1.5, open_browser).start()