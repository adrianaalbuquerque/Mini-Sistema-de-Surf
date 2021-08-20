class Pais:
    def __init__(self, nome, lingua):
        self._nome = nome
        self._lingua = lingua
        self._praias = []

    def get_nome_pais(self):
        return self._nome
    
    def set_nome_pais(self, nome_pais):
        self._nome = nome_pais
    
    def get_lingua(self):
        return self._lingua
    
    def set_lingua(self, lingua):
        self._lingua = lingua
    
    def get_praias(self):
        return self._praias
    
    def set_praias(self, praias):
        self._praias = praias

    def praias_mais_selecionadas(self, quantidade):
        praias_mais_selecionadas = []
        for praia in self._praias:
          if praia.get_num_campeonatos_realizados() >= quantidade:
            praias_mais_selecionadas.append(praia)
        return praias_mais_selecionadas

    def adicionar_praia(self, praia):
      self._praias.append(praia)
      praia.set_pais(self)

    def __str__(self):
        return f"{self._nome}"