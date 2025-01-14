import uuid
from atributos import Atributo
from classes import Lenhador, Investigador, Estudioso, PopStar, GolpistaEmpresario, AtletaVigor, AtletaForca, Riquinho

class Personagem:
    def __init__(self, nome, classe, nivel):
        self.id = str(uuid.uuid4())  # Gerando um id único
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
        self.proficiencias = self.classe.definirProficiencias(self.classe)
        self.vida_rolada = 0
        self.vida = 0
        self.dn = 0

    def definirVidaRolada(self, vida_rolada):
        self.vida_rolada = vida_rolada
        vigor = self.get_atributo("Vigor").valor
        self.vida = self.classe.calcularVida(self.classe(),vigor, self.vida_rolada, self.nivel)

    def calcularDN(self):
        if(self.classe().nome != "Lenhador"):
            rapidez = self.get_atributo("Rapidez").valor
            self.dn = self.classe.calcularDN(self.classe(), rapidez)
        else:
            vigor = self.get_atributo("Vigor").valor
            self.dn = self.classe.calcularDN(self.classe(), vigor)
        return self.dn

    def get_atributo(self, nome):
        return next((attr for attr in self.atributos if attr.nome == nome), None)

    def to_dict(self):
        return {
            "id": self.id,  # Incluindo o id
            "nome": self.nome,
            "classe": self.classe().nome,
            "nivel": self.nivel,
            "atributos": [attr.to_dict() for attr in self.atributos],
            "vida_rolada": self.vida_rolada,
            "vida": self.vida,
            "dn": self.dn,
            "proficiencias": self.proficiencias,
        }

    @staticmethod
    def from_dict(data, classes_disponiveis):
        classe = classes_disponiveis.get(data["classe"])
        personagem = Personagem(data["nome"], classe, data["nivel"])
        personagem.id = data["id"]
        personagem.vida_rolada = data["vida_rolada"]
        personagem.vida = data["vida"]
        personagem.dn = data["dn"]
        personagem.atributos = [Atributo.from_dict(attr) for attr in data["atributos"]]
        return personagem
