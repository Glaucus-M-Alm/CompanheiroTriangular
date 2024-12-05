import json
import os

class Database:
    def __init__(self, arquivo_banco="../data/fichas.json"):
        self.arquivo_banco = arquivo_banco
        self.fichas = []
        self.carregar_fichas()

    def carregar_fichas(self):
        if os.path.exists(self.arquivo_banco):
            with open(self.arquivo_banco, "r") as f:
                self.fichas = json.load(f)
        else:
            self.fichas = []

    def salvar_fichas(self):
        with open(self.arquivo_banco, "w") as f:
            json.dump(self.fichas, f, indent=4)

    def listar_fichas(self):
        return self.fichas

    def adicionar_ficha(self, ficha):
        self.fichas.append(ficha)
        self.salvar_fichas()

    def remover_ficha(self, nome):
        self.fichas = [ficha for ficha in self.fichas if ficha["nome"] != nome]
        self.salvar_fichas()
