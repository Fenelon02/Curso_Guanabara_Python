'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
'''
import time
import random
gaurado=[]
jogadas=int(input('Digite a quantidade de vezes que quer jogar: '))

for numeros in range(0,jogadas):

    numeros_aleatorios=random.sample(range(1, 61),6)

    # o sample gera coisas aleatórias, transformando em listas, sem repetições, exemplo: ('elemento', 6)
    #neste caso o 6 indica a quantidade de elementos que deseja, podendo ser int etc

    gaurado.append(numeros_aleatorios[:])


print('Aqui estão suas jogadas')

for numeros_apostados in range(len(gaurado)):

    time.sleep(1)
    print(f'Jogada número {numeros_apostados+1}: {sorted(gaurado[numeros_apostados])}')

print('Boa sorte',end='')
