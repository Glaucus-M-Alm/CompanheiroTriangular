import pandas as pd
import os

class Database:
    def __init__(self, arquivo='../data/database.json'):
        self.arquivo = arquivo
        if not os.path.exists(self.arquivo):
            pd.DataFrame().to_json(self.arquivo, orient="records", indent=4)

    def carregar_fichas(self):
        try:
            return pd.read_json(self.arquivo, orient="records")
        except ValueError:
            return pd.DataFrame()

    def salvar_fichas(self, df):
        df.to_json(self.arquivo, orient="records", indent=4)

    def listar_fichas(self):
        return self.carregar_fichas().to_dict(orient="records")

    def adicionar_ficha(self, ficha):
        df = self.carregar_fichas()
        nova_ficha = pd.DataFrame([ficha])
        df = pd.concat([df, nova_ficha], ignore_index=True)
        self.salvar_fichas(df)

    def editar_ficha(self, nome, novos_dados):
        df = self.carregar_fichas()
        if nome in df["nome"].values:
            for chave, valor in novos_dados.items():
                df.loc[df["nome"] == nome, chave] = valor
            self.salvar_fichas(df)
        else:
            raise ValueError(f"Ficha com o nome '{nome}' não encontrada.")

    def excluir_ficha(self, nome):
        df = self.carregar_fichas()
        if nome in df["nome"].values:
            df = df[df["nome"] != nome]
            self.salvar_fichas(df)
        else:
            raise ValueError(f"Ficha com o nome '{nome}' não encontrada.")
