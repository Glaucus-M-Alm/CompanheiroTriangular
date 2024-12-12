from InterfaceClasses import InterfaceClasses
class Lenhador(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if(vigorBonus >0):
            return vida_rolada+vigorBonus
        else:
            return vida_rolada
    def calcularDN(self, vigorBonus):
        return vigorBonus+6
class Estudioso(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if(vigorBonus >0):
            return vida_rolada+vigorBonus
        else:
            return vida_rolada
    def calcularDN(self, destrezaBonus):
        return destrezaBonus+
class Golpista(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if(vigorBonus >0):
            return vida_rolada+vigorBonus
        else:
            return vida_rolada
    def calcularDN(self, destrezaBonus):
        return destrezaBonus+6
class Investigador(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if(vigorBonus >0):
            return vida_rolada+vigorBonus
        else:
            return vida_rolada
    def calcularDN(self, destrezaBonus):
        return destrezaBonus+6
class PopStar(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if(vigorBonus >0):
            return vida_rolada+vigorBonus
        else:
            return vida_rolada
    def calcularDN(self, destrezaBonus):
        return destrezaBonus+6
class Atleta(InterfaceClasses):
    def calcularVida(self, vigorBonus, vida_rolada):
        if(vigorBonus >0):
            return vida_rolada+vigorBonus
        else:
            return vida_rolada
    def calcularDN(self, destrezaBonus):
        return destrezaBonus+6
