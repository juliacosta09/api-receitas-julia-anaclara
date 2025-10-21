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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="API de Receitas - Ana Clara e Júlia Emily")

class CreateReceita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

class Receita(CreateReceita):
    id: int

receitas: List[Receita] = []
ultimo_id = 0

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo ao Livro de Receitas!"}

@app.post("/receitas", response_model=Receita)
def criar_receita(dados: CreateReceita):
    global ultimo_id
    # Verifica se já existe uma receita com o mesmo nome
    for r in receitas:
        if r.nome.lower() == dados.nome.lower():
            raise HTTPException(status_code=400, detail="Receita já existe.")

    ultimo_id += 1
    nova_receita = Receita(id=ultimo_id, **dados.dict())
    receitas.append(nova_receita)
    return nova_receita

@app.get("/receitas", response_model=List[Receita])
def listar_receitas():
    return receitas

@app.get("/receitas/{id}", response_model=Receita)
def obter_receita(id: int):
    for receita in receitas:
        if receita.id == id:
            return receita
    raise HTTPException(status_code=404, detail="Receita não encontrada.")

@app.put("/receitas/{id}", response_model=Receita)
def atualizar_receita(id: int, dados: CreateReceita):
    for i, receita in enumerate(receitas):
        if receita.id == id:
            receita_atualizada = Receita(id=id, **dados.dict())
            receitas[i] = receita_atualizada
            return receita_atualizada
    raise HTTPException(status_code=404, detail="Receita não encontrada.")

@app.delete("/receitas/{id}")
def deletar_receita(id: int):
    for i, receita in enumerate(receitas):
        if receita.id == id:
            receitas.pop(i)
            return {"mensagem": f"Receita com id {id} deletada com sucesso."}
    raise HTTPException(status_code=404, detail="Receita não encontrada.")
