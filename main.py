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
]'''
from fastapi import FastAPI

from pydantic import BaseModel
from typing import List
class receita(BaseModel):
    nome : str
    ingredientes : List[str]
    modo_de_preparo : str

receitas: List[receita] = []

app = FastAPI(title='API da Ana Clara e da Júlia Emily')

@app.get("/")
def title():
    return {"title": "livro de receitas"}

@app.get("/receita")
def get_receita():
    return{"/"}

@app.get("/receitas/{nome_receita}")
def get_receita_by_name(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
          return receita

    return {"receita não encontrada"}

receitas: List[receita] = []

@app.get("/receitas/")
def get_todas_receitas():
    return receitas

@app.post("/receitas")
def create_receita(dados: receita):
    nova_receita = dados

    receitas.append(nova_receita)
    return nova_receita

from fastapi import FastAPI
app = FastAPI()
receitas = []

@app.post("/receitas/")
def criar_receita(nome: str, descricao: str):
     for r in receitas:
          if r[0] == nome:
               return "uma receita ja tem esse nome"
          receitas.append((nome, descricao))
          return "receita {nome} criada"
     
class CreateReceita(BaseModel):
        nome: str
        ingredientes: List[str]
        modo_de_preparo: str

class Receita(BaseModel):
        id: int
        nome: str
        ingredientes: List[str]
        modo_de_preparo: str

from fastapi import FastAPI
app = FastAPI()

receitas = []
ultimo_id = 0

@app.post("/receitas")
def criar_receita(nome: str , ingredientes: str , modo_de_preparo: str):
     ultimo_id[0] += 1
     receita = (ultimo_id[0], nome,ingredientes, modo_de_preparo)
     receitas.append(receita)
     return receita
