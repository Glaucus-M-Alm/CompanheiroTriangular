from classes.InterfaceClasses import InterfaceClasses

class Riquinho(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if vigorBonus > 0:
            return vida_rolada + vigorBonus
        return vida_rolada

    def calcularDN(self, rapidezBonus):
        return rapidezBonus + 6

    def definirProficiencias(self):
        return ["aparência", "vigor"]
