from classes.InterfaceClasses import InterfaceClasses

class PopStar(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if vigorBonus > 0:
            return vida_rolada + vigorBonus
        return vida_rolada

    def calcularDN(self, daoridadeBonus):
        return daoridadeBonus + 6

    def definirProficiencias(self):
        return ["aparência", "daoridade"]
