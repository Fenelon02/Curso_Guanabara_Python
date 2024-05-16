import random

numero_jogador=int(input('Digite um número: '))

lista=[1,2,3,4,5]

computador_escolhe_número= lista

x=random.choice(lista)


if numero_jogador==computador_escolhe_número:
    print('Parabéns, o número é igual')
else:
    print('Puts, número diferente')


print(f'O número escolhido pelo computador foi o {x}')
