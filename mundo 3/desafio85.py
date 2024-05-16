'''
 Crie um programa onde o usuário possa digitar sete valores numéricos,
 cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
 No final, mostre os valores pares e ímpares em ordem crescente.
'''
#Meu método
#fiz demasiadamente errado
'''
lista_total=[]
lista_impares=[]
lista_pares=[]

for numero in range(0,7):
    lista_total.append(int(input('Digite um valor: ')))

for unidade in lista_total:
    if unidade%2==0:
        lista_pares.append(unidade)
    if unidade%2!=0:
        lista_impares.append(unidade)

print(f'Os números ímpares são: {(sorted(lista_impares))}')
print(f'os números pares são: {(sorted(lista_pares))}')
'''

#guanabara
'''
lista_total=[[],[]]
numero=0

for contador in range(0,7):
    numero=(int(input('Digite um valor: ')))

    if numero%2==0:
        lista_total[0].append(numero)
    if numero%2!=0:
        lista_total[1].append(numero)



print(f'Os números ímpares são: {sorted(lista_total[1])}')
print(f'os números pares são: {sorted(lista_total[0])}')
'''











