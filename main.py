from surfista import Surfista
from campeonato import Campeonato
from pais import Pais
from prancha import Prancha
from praia import Praia

todos_surfistas = []
todos_campeonatos = []
todos_paises = []
todas_pranchas = []
todas_praias = []

def criar_surfistas():
  nomes = ["Stephanie Gilmore", "Sally Fitzgibbons", "Brisa Hennessy", "Tatiana Weston", "Grant Baker", "Lucas Chianca", "Natxo Gonzalez", "Alex Botelho", "Keala Kennelly", "Andrea Moller", "Emily Erickson", "Paige Alms", "Carissa Moore", "Tyler Wright", "Leticia Canales", "Connor O'Leary", "Matt Banting", "Owen Wright", "Ian Gentil", "Frederico Morais", "Ramzi Boukhiam", "Jorgann Couzinet", "Luel Felipe", "Gabriela Bryan", "Keala Tomoda-Bannert", "Leila Riccobuano", "Karelle Poppke"]
  idades = [33, 30, 21, 24, 47, 25, 25, 32, 43, 41, 31, 32, 28, 26, 26, 27, 26, 31, 25, 29, 27, 27, 29, 19, 23, 18, 26]

  for i in range(len(nomes)):
    novo_surfista = Surfista(nomes[i], idades[i])
    todos_surfistas.append(novo_surfista)

def criar_campeonatos():
  nomes = ["Corona Bali Protected", "Nazare Tow Surfing", "Jaws Challenge", "Sidney Surf Pro", "Vissla Central Coast Pro", "Pro Santa Cruz", "Papara Pro Vahine Open Tahiti"]
  premios = [100000, 100000, 20000, 25000, 15000, 1000, 15000]

  for i in range(len(nomes)):
    novo_campeonato = Campeonato(nomes[i], premios[i])
    todos_campeonatos.append(novo_campeonato)

def criar_paises():
  nomes = ["Indonésia", "Portugal", "EUA", "Austrália", "Australia", "Portugal", "França"]
  linguas = ["Indonésio", "Português", "Inglês", "Inglês", "Inglês", "Português", "Francês"]

  for i in range(0, len(nomes)):
    novo_pais = Pais(nomes[i], linguas[i])
    todos_paises.append(novo_pais)

def criar_pranchas():
  marcas = ["DVS", "Firewire", "Lost", "DVS", "Firewire", "Lost", "Lib Tech", "DVS", "Lib Tech", "Lib Tech", "Firewire", "Hayden Shapes", "Lost", "Firewire", "Lost", "DVS", "Firewire", "Lost", "DVS", "Firewire", "Lost", "Lib Tech", "DVS", "Firewire", "Lib Tech", "Firewire", "Hayden Shapes", "Lost", "Firewire", "Lib Tech", "DVS", "Lib Tech", "Lost", "Firewire", "Lost"]
  comprimentos = [2.15, 1.90, 2.25, 2.17, 2.20, 2.10, 2.15, 2, 1.85, 2.05, 2.20, 2.10, 2.14, 2.15, 2, 2.15, 1.90, 2, 2, 2, 2, 2, 2, 1.85, 2.05, 2.20, 2, 2, 1.98, 1.97, 2.35, 2.22, 2.15, 2.26, 2.30]
  cores = ["Rosa", "Azul", "Lilás", "Vermelho", "Vermelho", "Roxo", "Verde", "Verde", "Rosa", "Cinza", "Roxo", "Marrom", "Laranja", "Branco", "Oliva", "Azul", "Azul", "Lilás", "Oliva", "Vermelho", "Vermelho", "Verde", "Azul", "Rosa", "Cinza", "Verde", "Oliva", "Laranja", "Verde", "Vermelho", "Rosa", "Cinza", "Verde", "Amarelo", "Laranja"]
  valores = [7090, 4525, 3300, 4560, 4745, 4825, 8700, 9170, 5600, 2520, 2220, 4107, 3180, 2350, 13790, 4525, 3300, 2190, 4560, 4745, 4825, 8700, 9170, 5600, 2520, 2220, 4107, 3180, 9170, 5600, 2520, 2220, 4107, 3180, 8500]

  for i in range(len(marcas)):
    nova_prancha = Prancha(marcas[i], comprimentos[i], cores[i], valores[i])
    todas_pranchas.append(nova_prancha)

def criar_praias():
  nomes = ["Keramas", "Nazare", "Peahi", "Manly Beach", "Avoca Beach", "Papara"]

  for i in range(0, len(nomes)):
    nova_praia = Praia(nomes[i])
    todas_praias.append(nova_praia)

def main():
  print("Bem-vindo ao sistema de surf")
  criar_surfistas()
  criar_praias()
  criar_campeonatos()
  criar_paises()
  criar_pranchas()

  #criando os relacionamentos
  #surfistas

  todos_surfistas[0].set_pranchas(todas_pranchas[0:1])
  todos_surfistas[1].set_pranchas(todas_pranchas[1:3])
  todos_surfistas[2].set_pranchas(todas_pranchas[3:4])
  todos_surfistas[3].set_pranchas(todas_pranchas[4:5])
  todos_surfistas[4].set_pranchas(todas_pranchas[5:8])
  todos_surfistas[5].set_pranchas(todas_pranchas[8:9])
  todos_surfistas[6].set_pranchas(todas_pranchas[9:10])
  todos_surfistas[7].set_pranchas(todas_pranchas[10:11])
  todos_surfistas[8].set_pranchas(todas_pranchas[11:12])
  todos_surfistas[9].set_pranchas(todas_pranchas[12:15])
  todos_surfistas[10].set_pranchas(todas_pranchas[15:16])
  todos_surfistas[11].set_pranchas(todas_pranchas[16:17])
  todos_surfistas[12].set_pranchas(todas_pranchas[17:18])
  todos_surfistas[13].set_pranchas(todas_pranchas[18:19])
  todos_surfistas[14].set_pranchas(todas_pranchas[19:20])
  todos_surfistas[15].set_pranchas(todas_pranchas[20:21])
  todos_surfistas[16].set_pranchas(todas_pranchas[21:22])
  todos_surfistas[17].set_pranchas(todas_pranchas[22:23])
  todos_surfistas[18].set_pranchas(todas_pranchas[23:24])
  todos_surfistas[19].set_pranchas(todas_pranchas[24:25])
  todos_surfistas[20].set_pranchas(todas_pranchas[25:26])
  todos_surfistas[21].set_pranchas(todas_pranchas[26:27])
  todos_surfistas[22].set_pranchas(todas_pranchas[27:28])
  todos_surfistas[23].set_pranchas(todas_pranchas[28:30])
  todos_surfistas[24].set_pranchas(todas_pranchas[30:32])
  todos_surfistas[25].set_pranchas(todas_pranchas[32:34])
  todos_surfistas[26].set_pranchas(todas_pranchas[34])
  

  #campeonato 1
  todos_campeonatos[0].add_participante(todos_surfistas[0])
  todos_campeonatos[0].add_participante(todos_surfistas[1])
  todos_campeonatos[0].add_participante(todos_surfistas[2])
  todos_campeonatos[0].add_participante(todos_surfistas[3])
  todos_campeonatos[0].set_praia(todas_praias[0])
  todos_campeonatos[0].set_campeao(todos_surfistas[0])
  
  #Campeonato 2

  todos_campeonatos[1].add_participante(todos_surfistas[4])
  todos_campeonatos[1].add_participante(todos_surfistas[5])
  todos_campeonatos[1].add_participante(todos_surfistas[6])
  todos_campeonatos[1].add_participante(todos_surfistas[7])
  todos_campeonatos[1].set_praia(todas_praias[1])
  todos_campeonatos[1].set_campeao(todos_surfistas[4])

  #Campeonato 3

  todos_campeonatos[2].add_participante(todos_surfistas[8])
  todos_campeonatos[2].add_participante(todos_surfistas[9])
  todos_campeonatos[2].add_participante(todos_surfistas[10])
  todos_campeonatos[2].add_participante(todos_surfistas[11])
  todos_campeonatos[2].set_praia(todas_praias[1])
  todos_campeonatos[2].set_campeao(todos_surfistas[8])

  #Campeonato 4

  todos_campeonatos[3].add_participante(todos_surfistas[12])
  todos_campeonatos[3].add_participante(todos_surfistas[13])
  todos_campeonatos[3].add_participante(todos_surfistas[3])
  todos_campeonatos[3].add_participante(todos_surfistas[14])
  todos_campeonatos[3].set_praia(todas_praias[3])
  todos_campeonatos[3].set_campeao(todos_surfistas[12])
  
  #Campeonato 5

  todos_campeonatos[4].add_participante(todos_surfistas[15])
  todos_campeonatos[4].add_participante(todos_surfistas[16])
  todos_campeonatos[4].add_participante(todos_surfistas[17])
  todos_campeonatos[4].add_participante(todos_surfistas[18])
  todos_campeonatos[4].set_praia(todas_praias[4])
  todos_campeonatos[4].set_campeao(todos_surfistas[15])
  
  #Campeonato 6

  todos_campeonatos[5].add_participante(todos_surfistas[19])
  todos_campeonatos[5].add_participante(todos_surfistas[20])
  todos_campeonatos[5].add_participante(todos_surfistas[21])
  todos_campeonatos[5].add_participante(todos_surfistas[22])
  todos_campeonatos[5].set_praia(todas_praias[1])
  todos_campeonatos[5].set_campeao(todos_surfistas[19])

  #Campeonato 7

  todos_campeonatos[6].add_participante(todos_surfistas[23])
  todos_campeonatos[6].add_participante(todos_surfistas[24])
  todos_campeonatos[6].add_participante(todos_surfistas[25])
  todos_campeonatos[5].add_participante(todos_surfistas[26])
  todos_campeonatos[6].set_praia(todas_praias[5])
  todos_campeonatos[6].set_campeao(todos_surfistas[23])

  #países

  todos_paises[0].adicionar_praia(todas_praias[0])
  todos_paises[1].adicionar_praia(todas_praias[1])
  todos_paises[2].adicionar_praia(todas_praias[2])
  todos_paises[3].adicionar_praia(todas_praias[3])
  todos_paises[4].adicionar_praia(todas_praias[4])
  todos_paises[5].adicionar_praia(todas_praias[5])

  #pranchas

  todas_pranchas[0].set_fabricacao(todos_paises[3])
  todas_pranchas[1].set_fabricacao(todos_paises[3])
  todas_pranchas[2].set_fabricacao(todos_paises[2])
  todas_pranchas[3].set_fabricacao(todos_paises[3])
  todas_pranchas[4].set_fabricacao(todos_paises[3])
  todas_pranchas[5].set_fabricacao(todos_paises[2])
  todas_pranchas[6].set_fabricacao(todos_paises[2])
  todas_pranchas[7].set_fabricacao(todos_paises[3])
  todas_pranchas[8].set_fabricacao(todos_paises[2])
  todas_pranchas[9].set_fabricacao(todos_paises[2])
  todas_pranchas[10].set_fabricacao(todos_paises[3])
  todas_pranchas[11].set_fabricacao(todos_paises[3])
  todas_pranchas[12].set_fabricacao(todos_paises[2])
  todas_pranchas[13].set_fabricacao(todos_paises[3])
  todas_pranchas[14].set_fabricacao(todos_paises[2])
  todas_pranchas[15].set_fabricacao(todos_paises[3])
  todas_pranchas[16].set_fabricacao(todos_paises[3])
  todas_pranchas[17].set_fabricacao(todos_paises[2])
  todas_pranchas[18].set_fabricacao(todos_paises[3])
  todas_pranchas[19].set_fabricacao(todos_paises[3])
  todas_pranchas[20].set_fabricacao(todos_paises[2])
  todas_pranchas[21].set_fabricacao(todos_paises[2])
  todas_pranchas[22].set_fabricacao(todos_paises[3])
  todas_pranchas[23].set_fabricacao(todos_paises[3])
  todas_pranchas[24].set_fabricacao(todos_paises[2])
  todas_pranchas[25].set_fabricacao(todos_paises[3])
  todas_pranchas[26].set_fabricacao(todos_paises[3])
  todas_pranchas[27].set_fabricacao(todos_paises[2])
  todas_pranchas[28].set_fabricacao(todos_paises[3])
  todas_pranchas[29].set_fabricacao(todos_paises[2])
  todas_pranchas[30].set_fabricacao(todos_paises[3])
  todas_pranchas[31].set_fabricacao(todos_paises[2])
  todas_pranchas[32].set_fabricacao(todos_paises[2])
  todas_pranchas[33].set_fabricacao(todos_paises[3])
  todas_pranchas[34].set_fabricacao(todos_paises[2])
  
  #menu

  print("Seja bem-vindo ao sistema de surf! Escolha uma das opções abaixo:")
  print("----------------------------------------------------------------------------------------------")
  while True:
    print("[1] Consultar praias mais selecionadas")
    print("[2] Consultar maior e menor idades dos participantes de um campeonato por surfista campeão")
    print("[3] Consultar total ganho por um surfista em todos os campeonatos que participou")
    print("[4] Consultar nomes dos surfistas que participaram de um determinado campeonato")
    print("[5] Total gasto com pranchas por surfista")
    print("[6] Total de pranchas fabricadas por um determinado país")
    print("[X] Sair")
    opcao_escolhida = input("Digite a opção desejada: ")
    print("--------------------------------------------------------------------------------------------")

    if opcao_escolhida == "1":
      quantidade_escolhida = int(input("Digite a quantidade mínima de campeonatos realizados:"))
      praias_mais_selecionadas = []
      for pais in todos_paises:
        praias_mais_selecionadas_do_pais = pais.praias_mais_selecionadas(quantidade_escolhida)
        if len(praias_mais_selecionadas_do_pais) > 0:
          praias_mais_selecionadas.extend(praias_mais_selecionadas_do_pais)
          for praia_mais_selecionada in praias_mais_selecionadas:
            print(f"Praias mais selecionadas de acordo com a quantidade {quantidade_escolhida}: {praia_mais_selecionada}")

    elif opcao_escolhida == "2":
      nome_surfista = input("Digite o nome do surfista campeão:")
      campeonatos_ganhos_por_surfista = []
      for campeonato in todos_campeonatos:
        if campeonato.get_campeao().get_nome() == nome_surfista:
          campeonatos_ganhos_por_surfista.append(campeonato)
      if len(campeonatos_ganhos_por_surfista) > 0:
        for campeonato in campeonatos_ganhos_por_surfista:
          print(f"Encontramos o surfista selecionado no campeonato: {campeonato}")
          print(f"Maior idade dos participantes desse campeonato: {campeonato.maior_idade()}")
          print(f"Menor idade dos participantes desse campeonato: {campeonato.menor_idade()}")
      else:
        print("Esse surfista não existe ou não ganhou um campeonato")
    elif opcao_escolhida == "3":
      nome_surfista = input("Digite o nome do surfista:")
      surfista_encontrado = None
      for surfista in todos_surfistas:
        if surfista.get_nome() == nome_surfista:
          surfista_encontrado = surfista

      if (surfista_encontrado != None):
        campeonatos_ganhos_por_surfista = []
        for campeonato in todos_campeonatos:
          if campeonato.get_campeao() == surfista_encontrado:
            campeonatos_ganhos_por_surfista.append(campeonato)
        total_ganho = 0
        for campeonato_ganho in campeonatos_ganhos_por_surfista:
          total_ganho += campeonato_ganho.get_premio()
        print(f"O surfista {nome_surfista} ganhou o total de R$ {total_ganho} somando todos os campeonatos que participou")
      else:
        print(f"O surfista {nome_surfista} não foi encontrado") 

    elif opcao_escolhida == "4":
      nome_campeonato = input("Digite o nome do campeonato:")
      campeonato_encontrado = None
      for campeonato in todos_campeonatos:
        if campeonato.get_nome_campeonato() == nome_campeonato:
          campeonato_encontrado = campeonato
      if (campeonato_encontrado != None):
        print(f"A lista dos surfistas participantes do campeonato {campeonato_encontrado.get_nome_campeonato()}:")
        campeonato_encontrado.imprime_surfistas()
      else:
        print(f"O campeonato {nome_campeonato} não foi encontrado")

    elif opcao_escolhida == "5":
      nome_surfista = input("Digite o nome do surfista:")
      surfista_encontrado = None
      for surfista in todos_surfistas:
        if surfista.get_nome() == nome_surfista:
          surfista_encontrado = surfista
      if (surfista_encontrado != None):
        total_gasto = 0
        for prancha in surfista_encontrado.get_pranchas():
          total_gasto += prancha.get_valor()
        print(f"O surfista {nome_surfista} gastou o total de R$ {total_gasto} com pranchas")
      else:
        print(f"O surfista {nome_surfista} não foi encontrado")   

    elif opcao_escolhida == "6":
      nome_pais = input("Digite o nome do país:")
      pais_encontrado = None
      for pais in todos_paises:
        if pais.get_nome_pais() == nome_pais:
          pais_encontrado = pais
      if (pais_encontrado != None):
        quantidade_pranchas_do_pais_escolhido = 0
        for prancha in todas_pranchas:
          if prancha.get_fabricacao() == pais_encontrado:
            quantidade_pranchas_do_pais_escolhido += 1
        print(f"A quantidade de pranchas fabricadas pelo país {nome_pais} foi {quantidade_pranchas_do_pais_escolhido}")
      else:
        print(f"O país {nome_pais} não foi encontrado")
    else:
      break

if __name__ == "__main__":
  main()