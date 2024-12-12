from abc import ABC, abstractmethod
class InterfaceClasses(ABC):
    @abstractmethod
    def calcularVida(self):
        pass
    @abstractmethod
    def calcularDN(self):
        pass