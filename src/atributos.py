class Atributo:
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
        if -4 <= valor <= 6:
            self.__valor = valor
        else:
            raise ValueError(f"O valor do atributo '{self.__nome}' deve estar entre -4 e 6.")

    # Método getter para valor (opcional, mas incluído para consistência)
    def getValor(self):
        return self.__valor

    # Representação em string
    def __str__(self):
        return f"{self.__nome}: {self.__valor}"
