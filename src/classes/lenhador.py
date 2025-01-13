from classes.InterfaceClasses import InterfaceClasses

class Lenhador(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada, nivel):
        return vida_rolada + (vigorBonus * nivel) if vigorBonus > 0 else vida_rolada

    def calcularDN(self, vigorBonus):
        return vigorBonus + 6

    def definirProficiencias(self):
        return ["Vigor", "Força"]
