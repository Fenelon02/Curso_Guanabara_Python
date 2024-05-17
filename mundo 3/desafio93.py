'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.
'''

feitos_do_jogador={}
gols_total=[]

feitos_do_jogador['nome']=input('Qual nome do jogador? ')
feitos_do_jogador['partidas']=int(input('Quantas partidas ele jogou? '))

for i in range(feitos_do_jogador['partidas']):
    gol=int(input(f'na {i+1} partida, quantos gols ele fez? '))

    gols_total.append(gol)
    feitos_do_jogador['gol']=gols_total

    feitos_do_jogador['total']=sum(gols_total)
    #o sum() vai fazer a soma de tudo que está incluso em gols_total

print(feitos_do_jogador)
print('=-'*30)

for key,value in feitos_do_jogador.items():
    print(f'o campo {key} tem o valor {value}')

print('=-'*30)

print(f'O jogador {feitos_do_jogador["nome"]} jogou {feitos_do_jogador["partidas"]} partidas.')

for contador in range(feitos_do_jogador['partidas']):
    print(f'Na partida {contador+1}, fez {feitos_do_jogador["gol"][contador]} gols.')
print(f'Foi um total de {feitos_do_jogador["total"]} gols.')
