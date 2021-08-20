class Prancha:
    def __init__(self, marca, comprimento, cor, valor):
        self._marca = marca
        self._comprimento = comprimento
        self._cor = cor
        self._valor = valor
        self._fabricacao = None

    def get_marca(self):
        return self._marca

    def set_marca(self, nova_marca):
        self._marca = nova_marca
        
    def get_cor(self):
        return self._cor

    def set_cor(self, cor):
        self._cor = cor

    def get_valor(self):
        return self._valor

    def set_valor(self, valor):
        self._valor = valor

    def get_comprimento(self):
        return self._comprimento

    def set_comprimento(self, comprimento):
        self._comprimento = comprimento

    def get_fabricacao(self):
        return self._fabricacao

    def set_fabricacao(self, fabricacao):
        self._fabricacao = fabricacao

    def __str__(self):
        return f"Marca da prancha:{self._marca} \nComprimento: {self._comprimento} \nCor: {self._cor} \nValor: R${self._valor} \nOrigem de Fabricação: {self._fabricacao}"