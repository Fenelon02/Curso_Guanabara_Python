'''
Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                      
A) Quantos números foram digitados.   
B) A lista de valores, ordenada de forma decrescente.            
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista=[]
numero_para_adcionar=int(input('Digite um número: '))
lista.append(numero_para_adcionar)
deseja_prosseguir=input('Deseja continuar? S/N ').lower().strip()[0]

while 's' in deseja_prosseguir:
    numero_para_adcionar=int(input('Digite um número: '))
    lista.append(numero_para_adcionar)
    deseja_prosseguir=input('Deseja continuar? S/N ').lower().strip()[0]

    
tamanho=len(lista)
lista.sort(reverse=True)

print(f'Você digitou {tamanho} elementos')
print(f'A lista em ordem decrescente ficou desta maneira {lista}')

if 5 in lista:
    print('O número 5 foi digitado, e está na lista')
else:
    print('O número 5 não foi digitado, e não está na lista')
