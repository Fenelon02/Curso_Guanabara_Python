'''
Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.
'''

# Meu método (está certo, mas não está dentro de todos os para,etros que ele propoe)

def informacoes_jogador(nome='desconhecido',gols=0):
    return f'O jogador {nome} fez {gols} gols'

nome_do_jogador=input('Digite o nome do jogador: ')
quantidade_de_gols=input('Quantidade de gols: ')

if nome_do_jogador=='':
    nome_do_jogador='desconhecido'

if quantidade_de_gols.isdigit():
    quantidade_de_gols = int(quantidade_de_gols)
    
else:
    quantidade_de_gols = 0


print(informacoes_jogador(nome_do_jogador,quantidade_de_gols))
    
# método guanabara + meu método misturado
def informacoes_jogador(nome='desconhecido',gols=0):
    print(f'O jogador {nome} fez {gols} gols')

nome_do_jogador=input('Digite o nome do jogador: ')
quantidade_de_gols=input('Quantidade de gols: ')

if quantidade_de_gols.isdigit():
    quantidade_de_gols = int(quantidade_de_gols)
    
else:
    quantidade_de_gols = 0

if nome_do_jogador=='':
    informacoes_jogador(gols=quantidade_de_gols)

else:
    informacoes_jogador(nome_do_jogador,quantidade_de_gols)


