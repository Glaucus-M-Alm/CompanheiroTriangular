class Atributo:
    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor
        self._proficiente = False

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor

    @property
    def proficiente(self):
        return self._proficiente

    @proficiente.setter
    def proficiente(self, status):
        self._proficiente = status

    @property
    def bonus(self):
        return max(-4, min(6, self._valor))

    def __str__(self):
        return f"{self.nome.capitalize()}: {self.valor} (Proficiente: {'Sim' if self.proficiente else 'Não'})"
