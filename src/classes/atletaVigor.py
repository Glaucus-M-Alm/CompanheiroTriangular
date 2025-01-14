from classes.InterfaceClasses import InterfaceClasses

class AtletaVigor(InterfaceClasses):
    def __init__(self):
        self.nome="Atleta"

    def calcularVida(self, vigorBonus, vida_rolada, nivel):
        return vida_rolada + (vigorBonus * nivel) if vigorBonus > 0 else vida_rolada

    def calcularDN(self, rapidezBonus):
        return rapidezBonus + 6

    def definirProficiencias(self):
        return ["Rapidez e Vigor"]
