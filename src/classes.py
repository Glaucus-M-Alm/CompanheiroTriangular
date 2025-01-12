from InterfaceClasses import InterfaceClasses
from atributos import Atributo
class Lenhador(InterfaceClasses):
    def calcular_vida(self, vigor, nivel, vida_rolada):
        return nivel * max(0, vigor) + vida_rolada #valores de vigor negativos são
        #transformados em 0 para o cálculo de vida, usando o max(0, vigor) ele selecionará o que for maior 0 ou vigor
    def calcularDN(self, vigorBonus):
        return vigorBonus+6
    def definirProficiencias(self, atributos):
        atributos["força"].proficiente = True
        atributos["vigor"].proficiente = True
class Estudioso(InterfaceClasses):
    def calcular_vida(self, vigor, nivel, vida_rolada):
        return nivel * max(0, vigor) + vida_rolada
    def calcularDN(self, rapidezBonus):
        return rapidezBonus+
    def definirProficiencias(self, atributos):
        atributos["força"].proficiente = True
        atributos["vigor"].proficiente = True
class Golpista(InterfaceClasses):
    def calcular_vida(self, vigor, nivel, vida_rolada):
        return nivel * max(0, vigor) + vida_rolada
    def calcularDN(self, rapidezBonus):
        return rapidezBonus+6
class Investigador(InterfaceClasses):
    def calcular_vida(self, vigor, nivel, vida_rolada):
        return nivel * max(0, vigor) + vida_rolada
    def calcularDN(self, rapidezBonus):
        return rapidezBonus+6
class PopStar(InterfaceClasses):
    def calcular_vida(self, vigor, nivel, vida_rolada):
        return nivel * max(0, vigor) + vida_rolada
    def calcularDN(self, rapidezBonus):
        return rapidezBonus+6
class Atleta(InterfaceClasses):
    def calcular_vida(self, vigor, nivel, vida_rolada):
        return nivel * max(0, vigor) + vida_rolada
    def calcularDN(self, rapidezBonus):
        return rapidezBonus+6
