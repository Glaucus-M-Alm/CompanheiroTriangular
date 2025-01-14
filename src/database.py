import json
import os

class Database:
    def __init__(self, arquivo="fichas.json"):
        self.arquivo = arquivo

    def carregar_fichas(self):
        if not os.path.exists(self.arquivo):
            return {"fichas": []}

        with open(self.arquivo, "r") as file:
            return json.load(file)

    def salvar_fichas(self, dados):
        with open(self.arquivo, "w") as file:
            json.dump(dados, file, indent=4)

    def adicionar_ficha(self, ficha):
        dados = self.carregar_fichas()
        if "fichas" not in dados or not isinstance(dados["fichas"], list):
            dados["fichas"] = []
        dados["fichas"].append(ficha)
        self.salvar_fichas(dados)

    def listar_fichas(self):
        dados = self.carregar_fichas()
        return dados.get("fichas", [])

    def excluir_ficha(self, ficha_id):
        dados = self.carregar_fichas()
        fichas = dados.get("fichas", [])
        dados["fichas"] = [ficha for ficha in fichas if ficha["id"] != ficha_id]
        self.salvar_fichas(dados)

    def editar_ficha(self, ficha_id, nova_ficha):
        dados = self.carregar_fichas()
        fichas = dados.get("fichas", [])
        for i, ficha in enumerate(fichas):
            if ficha["id"] == ficha_id:
                fichas[i] = nova_ficha
                break
        dados["fichas"] = fichas
        self.salvar_fichas(dados)
