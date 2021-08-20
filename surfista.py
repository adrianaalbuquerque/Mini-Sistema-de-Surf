class Surfista:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._campeonatos = []
        self._pranchas = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome_surfista):
        self._nome = nome_surfista

    def get_idade(self):
        return self._idade

    def set_idade(self, idade_surfista):
        self._idade = idade_surfista

    def get_campeonatos(self):
        return self._campeonatos
    
    def set_campeonatos(self, campeonatos):
        self._campeonatos = campeonatos

    def get_pranchas(self):
        return self._pranchas

    def set_pranchas(self, pranchas):
        self._pranchas = pranchas

    def total_ganho(self):
        totalganho = 0
        for campeonato in self.get_campeonatos():
            if campeonato.get_campeao() == self:
                totalganho += campeonato.get_premio()
        return totalganho

    def pranchas_marca(self, marca):
        marca_prancha = []
        for prancha in self.get_pranchas():
            if prancha.get_marca() == marca:
                marca_prancha.append(prancha)
        return marca_prancha
    
    def campeonatos(self):
        print(f"Lista de Campeonatos que {self.get_nome()} participou:")
        for campeonato in self.get_campeonatos():
            print(campeonato)

    def __str__(self):
        return f"{self._nome}, {self._idade} anos"

