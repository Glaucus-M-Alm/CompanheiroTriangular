from classes.InterfaceClasses import InterfaceClasses

class GolpistaEmpresario(InterfaceClasses):
    def __init__(self):
        self.nome="Golpista/Empresário"
    def calcularVida(self, vigorBonus, vida_rolada, nivel):
        return vida_rolada + (vigorBonus * nivel) if vigorBonus > 0 else vida_rolada

    def calcularDN(self, daoridadeBonus):
        return daoridadeBonus + 6

    def definirProficiencias(self):
        return ["Inteligência", "Daoridade"]