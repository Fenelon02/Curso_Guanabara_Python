'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras 
que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista_completa=[]
lista_pares=[]
lista_impares=[]
deseja_continuar='s'

while 's' in deseja_continuar:
    numero=int(input('Digite um valor:'))

    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    lista_completa.append(numero)
    
    deseja_continuar=input('Deseja continuar? s/n ').lower().strip()[0]

    if deseja_continuar!='s':
        break

print(f'A lista com todos os números: {lista_completa}')
print(f'A lista com os números ímpares:{lista_impares}')
print(f'A lista com os números pares: {lista_pares}')
