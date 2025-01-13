from abc import ABC, abstractmethod

class InterfaceClasses(ABC):
    @abstractmethod
    def calcularVida(self, vigor_bonus, vida_rolada, nivel):
        pass

    @abstractmethod
    def calcularDN(self, atributo_bonus):
        pass

    @abstractmethod
    def definirProficiencias(self):
        pass
