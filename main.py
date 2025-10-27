'''receitas = [
    {
        "nome": "brownie",
        "ingredientes": ["3 ovos", "6 colheres de açúcar", "2 xícaras de chocolate em pó"],
        "utensilios": ["tigela", "forma"],
        "modo_preparo": "Misture tudo e leve ao forno por 40 minutos."
    },
    {
        "nome": "torta",
        "ingredientes": ["3 ovos", "1 xícara de leite", "2 xícaras de farinha"],
        "utensilios": ["liquidificador", "forma"],
        "modo_preparo": "Bata tudo no liquidificador e asse por 30 minutos."
    },
    {
        "nome": "bolo de cenoura",
        "ingredientes": ["3 cenouras", "3 ovos", "2 xícaras de açúcar"],
        "utensilios": ["liquidificador", "forma"],
        "modo_preparo": "Bata os ingredientes e asse por 40 minutos."
    },
]
  [
 {
        "nome": "panqueca",
        "ingredientes": ["2 ovos", "1 xícara de leite", "1 xícara de farinha"],
        "utensilios": ["frigideira"],
        "modo_preparo": "Bata tudo, despeje na frigideira e recheie a gosto."
    },
    {
        "nome": "pudim",
        "ingredientes": ["1 lata de leite condensado", "2 latas de leite", "3 ovos"],
        "utensilios": ["liquidificador", "forma de pudim"],
        "modo_preparo": "Bata, caramelize a forma e cozinhe em banho-maria."
    },
    {
        "nome": "mousse de maracujá",
        "ingredientes": ["1 lata de leite condensado", "1 lata de creme de leite", "suco de maracujá"],
        "utensilios": ["liquidificador"],
        "modo_preparo": "Bata tudo no liquidificador e leve à geladeira."
    }
]
  
]'''
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="API de Receitas - Ana Clara e Júlia Emily")

class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

receitas = []
ultimo_id = 0

@app.get("/")
def inicio():
    return {"mensagem": "Bem-vindo ao livro de receitas"}

@app.get("/receitas")
def ver_todas():
    return receitas

@app.get("/receitas/{id}")
def ver_por_id(id: int):
    for r in receitas:
        if r["id"] == id:
            return r
    return {"mensagem": "Receita não encontrada"}

@app.post("/receitas")
def criar_receita(nome: str, ingredientes: List[str], modo_de_preparo: str):
    global ultimo_id
    for r in receitas:
        if r["nome"] == nome:
            return {"mensagem": "Já existe uma receita com esse nome"}
    ultimo_id = ultimo_id + 1
    receita = {
        "id": ultimo_id,
        "nome": nome,
        "ingredientes": ingredientes,
        "modo_de_preparo": modo_de_preparo
    }
    receitas.append(receita)
    return {"mensagem": "Receita criada com sucesso", "receita": receita}

@app.put("/receitas/{id}")
def atualizar_receita(id: int, nome: str, ingredientes: List[str], modo_de_preparo: str):
    for r in receitas:
        if r["id"] == id:
            r["nome"] = nome
            r["ingredientes"] = ingredientes
            r["modo_de_preparo"] = modo_de_preparo
            return {"mensagem": "Receita atualizada com sucesso"}
    return {"mensagem": "Receita não encontrada"}

@app.delete("/receitas/{id}")
def deletar_receita(id: int):
    for r in receitas:
        if r["id"] == id:
            receitas.remove(r)
            return {"mensagem": "Receita deletada com sucesso"}
    return {"mensagem": "Receita não encontrada"}
