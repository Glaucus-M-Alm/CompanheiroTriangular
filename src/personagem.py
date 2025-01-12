from atributos import Atributo

class Personagem:
    def __init__(self, nome, classe, atributos, nivel):
        self.nome = nome
        self.classe = classe  # Instância de uma subclasse de Classes
        self.atributos = {key: Atributo(key, valor) for key, valor in atributos.items()}
        self.vida_rolada = 0
        self.nivel = nivel

        # Definir proficiências da classe
        self.classe.definir_proficiencias(self.atributos)

    @property
    def vida(self):
        return self.classe.calcular_vida(
            self.atributos["vigor"].valor, self.nivel, self.vida_rolada
        )

    @property
    def dn(self):
        return 10 + self.atributos["rapidez"].bonus

    def __str__(self):
        atributos_str = "\n".join(str(attr) for attr in self.atributos.values())
        return f"Nome: {self.nome}\nClasse: {self.classe.__class__.__name__}\nNível: {self.nivel}\nVida: {self.vida}\nAtributos:\n{atributos_str}"
