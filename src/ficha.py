class Ficha:
    def __init__(self, nome, classe, nivel, atributos):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.atributos = atributos

    def __str__(self):
        return f"Nome: {self.nome}, Classe: {self.classe}, Nível: {self.nivel}, Atributos: {self.atributos}"

    def to_dict(self):
        return {
            "nome": self.nome,
            "classe": self.classe,
            "nivel": self.nivel,
            "atributos": self.atributos,
        }
