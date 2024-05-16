from math import sqrt

'''Descobrir se um número é primo'''

vezes=int(input('quantidade de vezes que quer repetir: '))

for c in range(1, vezes):
    numero=int(input('Digite um numero e saiba se ele é ou não primo: '))

    if numero%2!=0 and sqrt(numero)!=int:
        print('Número primo')
    elif numero==2:
        print('Numero primo')
    else:
        print('Numero nao primo')