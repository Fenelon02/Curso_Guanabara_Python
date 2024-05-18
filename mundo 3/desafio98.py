'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            
a) de 1 até 10, de 1 em 1                                                    
b) de 10 até 0, de 2 em 2                                                                                                                                            
c) uma contagem personalizada
'''

from time import sleep

def linha():
    print('='*30)

def contagem(): 
    linha()
    print('Contagem de 1 até 10, de 1 em 1 ')  
    linha()
    for contador in range(1,11):
        #  flush é usado pra forçar que o resultado apareça imediatamente, mesmo sem linha nova.
        print(f' {contador}',end='',flush=True)
        sleep(0.5)
    print(' fim')

def contagem_10_2():
    linha()
    print('Contagem de 10 até 0, de 2 em 2')
    linha()
    contador=10
    while contador>=0:
        print(f' {contador}',end='',flush=True)
        sleep(0.5)
        contador-=2
    print(' Fim')


contagem()
contagem_10_2()


def contagem_personalizada(inicio,fim,pular):
    if pular<0:
        pular*=-1
        
    linha()
    print(f'Contagem de {inicio} até {fim} pulando de {pular} em {pular}.')
    linha()
    numero=inicio

    while fim<=numero:
        numeros=[]
        # numero-=pular
        if numero not in numeros:
            if numero>=fim:
                numeros.append(numero)

        numero-=pular

        for item in numeros:
            print(f' {item}',end='',flush=True)
            sleep(0.5)
    print(' fim')

linha()
print('Contagem personalizada')
linha()

inicio=float(input('Digite um número para começar: '))
fim=float(input('Digite um número para terminar: '))
pular=int(input('Digite a quantidade de casas para pular: '))

contagem_personalizada(inicio,fim,pular)

#CÓDIGO GUANABARA
'''
def contador(inicio,fim,passos):

    if passos<0:
        passos*=-1

    if inicio<fim:
        contador=inicio
        while contador<=fim:
            print(f' {contador}',end='',flush=True)
            sleep(0.5)
            contador+=passos
        print(' FIM')

    if inicio>fim:
        contador=inicio
        while contador>=fim:
            print(f' {contador}',end='',flush=True)
            sleep(0.5)
            contador-=passos
        print(' FIM')
    
contador(1,10,1)
contador(10,0,2)
inicio=int(input('Digite o início: '))    
fim=int(input('Digite o fim: '))
passos=int(input('Digite quantos passos quer pular: '))
contador(inicio,fim,passos)
'''