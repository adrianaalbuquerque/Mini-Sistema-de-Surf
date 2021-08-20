class Campeonato:
    def __init__(self, nome_do_campeonato, premio):
        self._nome_do_campeonato = nome_do_campeonato
        self._premio = premio
        self._campeao = None
        self._praia = None
        self._surfistas = []

    def get_nome_campeonato(self):
        return self._nome_do_campeonato

    def set_nome_campeonato(self, nome_campeonato):
        self._nome_do_campeonato = nome_campeonato
    
    def get_premio(self):
        return self._premio
    
    def set_premio(self, premio):
        self._premio = premio
    
    def get_campeao(self):
        return self._campeao
    
    def set_campeao(self, campeao):
        if campeao in self._surfistas:
            self._campeao = campeao
        else:
            raise ValueError("Esse surfista não participou do campeonato.")
   
    def get_praia(self):
        return self._praia
    
    def set_praia(self, praia):
        self._praia = praia
        self._praia.set_num_campeonatos_realizados(self._praia.get_num_campeonatos_realizados() + 1)

    def get_surfistas(self):
        return self._surfistas

    def set_surfistas(self, surfistas):
        self._surfistas = surfistas
    
    def add_participante(self, surfista):
        self.get_surfistas().append(surfista)
        surfista.get_campeonatos().append(self)

    def menor_idade(self):
        menor_idade = 200
        for surfista in self._surfistas:
            if surfista.get_idade() < menor_idade:
                menor_idade = surfista.get_idade()
        return menor_idade

    def maior_idade(self):
        maior_idade = 0
        for surfista in self._surfistas:
            if surfista.get_idade() > maior_idade:
                maior_idade = surfista.get_idade()
        return maior_idade
    
    def imprime_surfistas(self):
        for s in self._surfistas:
            print(s)

    def __str__(self):
        return f"{self._nome_do_campeonato} \nPremio: U${self._premio:.2f} \nRealizado na praia: {self._praia} \nCampeão: {self._campeao}"

      
      