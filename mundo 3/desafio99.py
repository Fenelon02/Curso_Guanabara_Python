'''
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(*numeros):

    if len(numeros)==0:
        print('=-'*30)
        print('Foram informados 0 valores ao todo.\nO maior valor indormaod foi 0.')

    else:
        print('=-'*30)
        print(f'Foram informados {len(numeros)} valores ao todo.')
        print('Dos números',end='')
        for numero in numeros:
            print(f' {numero}', end='')
        print(f' o maior é {max(numeros)}.',)

maior(2,9,4,5,7,1)
maior(4,0,7)
maior(1,2)
maior(6)
maior()