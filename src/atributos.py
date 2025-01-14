class Atributo:
    VALOR_MIN = -4
    VALOR_MAX = 6

    def __init__(self, nome, valor=0):
        self.__nome = nome
        self.__valor = 0
        self.setValor(valor)  # Validação inicial

    # Propriedade para nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            raise ValueError("O nome do atributo deve ser uma string não vazia.")

    # Propriedade para valor
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        self.setValor(novo_valor)

    # Método setter para valor com validação
    def setValor(self, valor):
        if self.VALOR_MIN <= valor <= self.VALOR_MAX:
            self.__valor = valor
        else:
            raise ValueError(f"O valor do atributo '{self.__nome}' deve estar entre {self.VALOR_MIN} e {self.VALOR_MAX}.")

    # Método getter para valor
    def getValor(self):
        return self.__valor

    # Representação em string
    def __str__(self):
        return f"{self.__nome}: {self.__valor}"

    # Representação para depuração
    def __repr__(self):
        return f"Atributo(nome='{self.__nome}', valor={self.__valor})"

    # Serialização para dicionário
    def to_dict(self):
        return {"nome": self.__nome, "valor": self.__valor}

    # Desserialização de dicionário
    @staticmethod
    def from_dict(data):
        return Atributo(data["nome"], data["valor"])
