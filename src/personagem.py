from ficha import Ficha
class Personagem(Ficha):
    def __init__(self, nome, classe, nivel, atributos, habilidades):
        super().__init__(nome, classe, nivel, atributos)
        self.habilidades = habilidades

    def __str__(self):
        base = super().__str__()
        return f"{base}, Habilidades: {self.habilidades}"

    def to_dict(self):
        return {
            "nome": self.nome,
            "classe": self.classe,
            "nivel": self.nivel,
            "atributos": self.atributos,
            "habilidades": self.habilidades,
        }
