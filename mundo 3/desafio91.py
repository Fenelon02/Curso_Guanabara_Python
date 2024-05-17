'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from operator import itemgetter
#meu código inicial
'''
informacoes_dos_jogadores=list()
numero_do_dado_e_numero_do_jogador=dict()
contador_lugar=1


for contador in range(0,4):
    numero_do_dado_e_numero_do_jogador['valor jogado']=randint(1,6)
    numero_do_dado_e_numero_do_jogador['nome do jogador']=contador+1

    informacoes_dos_jogadores.append(numero_do_dado_e_numero_do_jogador.copy())

for contador_2 in range(4):
    print(f'O jogador N{informacoes_dos_jogadores[contador_2]['nome do jogador']} jogou o número {informacoes_dos_jogadores[contador_2]['valor jogado']}')

informacoes_dos_jogadores.sort(key=lambda  x:x['valor jogado'],reverse=True)

print()
for jogador in informacoes_dos_jogadores:
    print(f'{contador_lugar} lugar: Jogador n{jogador['nome do jogador']} jogou o número {jogador['valor jogado']}')
    contador_lugar+=1
'''
#código novo guanabara
ranking=[]
jogo={'jogador 1':randint(1,6),
      'jogador 2':randint(1,6),
      'jogador 3':randint(1,6),
      'jogador 4':randint(1,6)}

for key,value in jogo.items():
    print(f'O {key} jogou {value}')

ranking=sorted(jogo.items(), key=itemgetter(1),reverse=True)
#este itemgetter (1) significa qe é para pegar o número

for contador,pessoa_e_colocação in enumerate(ranking):
    print(f'{contador+1} Lugar: {pessoa_e_colocação[0]} que jogou {pessoa_e_colocação[1]}')

