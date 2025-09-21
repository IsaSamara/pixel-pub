from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API Pixel Pub!"}

@app.get("/saudacao/{nome}")
def saudacao(nome: str):
    return {"mensagem": f"Saudações, {nome}!"}