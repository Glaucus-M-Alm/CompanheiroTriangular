from classes.InterfaceClasses import InterfaceClasses

class Atleta(InterfaceClasses):
    def __init__(self):
        self.proficiencia_opcoes = ["Rapidez e Força", "Rapidez e Vigor"]
        self.proficiencia_escolhida = None

    def calcularVida(self, vigorBonus, vida_rolada, nivel):
        return vida_rolada + (vigorBonus * nivel) if vigorBonus > 0 else vida_rolada

    def calcularDN(self, rapidezBonus):
        return rapidezBonus + 6

    def definirProficiencias(self):
        return self.proficiencia_escolhida
