'''
Faça um programa que tenha uma lista chamada números 
e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

numeros=[]

def sorteia():
    print(f'Sorteando 5 valores para a lista:',end='')

    for contador in range(0,5):
        numeros_gerado=randint(0,9)
        numeros.append(numeros_gerado)

    for item in numeros:
        print(f' {item}',end='',flush=True)
        sleep(0.5)

    print(' pronto!')
    

def soma_numeros_pares():
    total_soma_pares=0
    for item in numeros:
        if item%2==0:
            total_soma_pares+=item
    print(f'O total da soma de todos os números pares da lista {numeros} é {total_soma_pares}.')


sorteia()  
soma_numeros_pares()

