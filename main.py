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

class CreateReceita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str
    receitas: List[Receita] = []

class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

@app.get("/")
def hello():
    return {"title": "Livro de Receitas"}

@app.get("/receitas/{nome_receita}")
def buscar_por_nome(nome_receita: str):
    for receita in receita:
        if receita.nome == nome_receita:
            return {"mensagem": "Receita encontrada com sucesso!", "dados": receita}
    return {"mensagem": "Receita não encontrada."}

@app.get("/receitas")
def get_todas_receitas():
    return receita

@app.post("/receitas")
def create_receita(dados: CreateReceita):
    for receita in receita:
        if receita.nome == dados.nome:
            return {"mensagem": "essa receita ja existe"}
        ultimo-id=0
        for receita in receita:
            ultimo_id = receita.id
            novo_id=ultimo_id+1

            nova_receita = Receita(
                id=novo_id,
                nomes=dados.nome,
            ingredientes=dados.ingredientes,
            modo_de_preparo=dados.modo_de_preparo
            )

            receita.append(nova_receita)
            return {
                "mensagem": "Receita criada",
                "receita": nova_receita
            }
    
    @app.get("/receitas/id/{id}")
    def get_receita_por_id(id: int):
        for receita in receita:
            if receita.id == id:
                return receita
            return {"mensagem": "Receita nao encontrada"}
        

@app.put("/receitas/{id}")
def update_receita(id: int, dados: CreateReceita):
    if dados.nome == "" or dados.modo_de_preparo == "" or not dados.ingredientes:
        return {"mensagem": "Nenhum campo pode estar vazio."}

    for receita in receita:
        if receita.nome == dados.nome and receita.id != id:
            return {"mensagem": "Já existe uma receita com esse nome."}

    posicao = 0
    for receita in receita:
        if receita.id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo
            )
            receita[posicao] = receita_atualizada
            return {"mensagem": "Receita atualizada com sucesso!", "receita": receita_atualizada}
        posicao = posicao + 1

    return {"mensagem": "Receita não encontrada."}

@app.delete("/receitas/{id}")
def deletar_receita(id: int):
    for i in range (len(receitas)):
        if receitas[i].id == id:
            receitas.pop(i)
            return {"mensagem": "receita deletada"}
        return {"mensagem": "receita não econtrada"}
    
    @app.delete("/receitas/{id}")
    def deletar_receita(id: int):
        if not receitas:
            return {"mensagem": "sem receitas para deletar"}
        
        for i in range (len(receitas)):
            if receitas[i].id == id:
                nome_receita_deletada = receita[i].nome
                receitas.pop(i)

                return {
                    "mensagem": "receita foi apagada",
                    "receita_deletada": nome_receita_deletada
                }

        return {"mensagem": "receita não encontrada"}