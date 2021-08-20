class Praia:
    def __init__(self, nome):
        self._nome = nome
        self._pais = None
        self._num_campeonatos_realizados = 0

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_pais(self):
        return self._pais

    def set_pais(self, pais):
        self._pais = pais

    def get_num_campeonatos_realizados(self):
        return self._num_campeonatos_realizados

    def set_num_campeonatos_realizados(self, num_campeonatos_realizados):
        self._num_campeonatos_realizados = num_campeonatos_realizados

    def __str__(self):
        return f"{self._nome}"
