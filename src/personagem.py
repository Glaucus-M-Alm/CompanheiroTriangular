from atributos import Atributo
from classes import Lenhador, Investigador, Estudioso, PopStar, GolpistaEmpresario, Atleta, Riquinho

class Personagem:
    def __init__(self, nome, classe, nivel):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.atributos = [
            Atributo("Forca"),
            Atributo("Inteligencia"),
            Atributo("Rapidez"),
            Atributo("Vigor"),
            Atributo("Aparencia"),
            Atributo("Daoridade"),
        ]
        self.proficiencias = self.classe.definirProficiencias()
        self.vida_rolada = 0
        self.vida = 0
        self.dn = 0

    def definirVidaRolada(self, vida_rolada):
        self.vida_rolada = vida_rolada
        vigor = next(attr.valor for attr in self.atributos if attr.nome == "Vigor")
        self.vida = self.classe.calcularVida(vigor, self.vida_rolada, self.nivel)

    def calcularDN(self):
        rapidez = next(attr.valor for attr in self.atributos if attr.nome == "Rapidez")
        self.dn = self.classe.calcularDN(rapidez)
        return self.dn

    def __str__(self):
        atributos_str = ", ".join(str(atributo) for atributo in self.atributos)
        return (
            f"Personagem: {self.nome}\n"
            f"Classe: {self.classe.__class__.__name__}\n"
            f"Nível: {self.nivel}\n"
            f"Atributos: {atributos_str}\n"
            f"Vida: {self.vida}\n"
            f"DN: {self.dn}\n"
            f"Proficiencias: {', '.join(self.proficiencias)}"
        )
