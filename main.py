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

app = FastAPI(title="API de Receitas da Ana Clara e da Júlia Emily")

class Receita(BaseModel):

    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

@app.get("/")
def hello():
    return {"title": "Livro de Receitas"}

@app.get("/receitas")
def listar_receitas():
    return receitas

@app.get("/receitas/{nome_receita}")
def buscar_por_nome(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return {"mensagem": "Receita encontrada com sucesso!", "dados": receita}
    return {"mensagem": "Receita não encontrada."}

@app.post("/receitas")
def criar_receita(nova_receita: Receita):
    for r in receitas:
        if r.nome == nova_receita.nome:
            return {"mensagem": "Já existe uma receita com esse nome."}
    receitas.append(nova_receita)
    return {"mensagem": "Receita criada com sucesso!", "dados": nova_receita}

@app.put("/receitas/{id}")
def atualizar_receita(id: int, dados: Receita):
    for receita in receitas:
        if receita.id == id:
            receitas.remove(receita)
            receitas.append(dados)
            return {"mensagem": "Receita atualizada", "dados": dados}
    return {"mensagem": "Receita não encontrada."}

@app.delete("/receitas/{nome_receita}")
def deletar_receita(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            receitas.remove(receita)
            return {"mensagem":"Receita deletada com sucesso!"}
    return {"mensagem": "A receita '{nome_receita}' não foi encontrada."}