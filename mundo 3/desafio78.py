#meu método

'''lista=[]

for valores in range(0,5):
    numero=float(input(f'Digite um valor para ocupar a posição {valores}: '))
    lista.append(numero)

maior=max(lista)
menor=min(lista)

posição_maior=lista.index(maior)

posição_menor=lista.index(menor)

print(f'A lista digitada foi: {lista}')
print(f'O maior elemento digitado foi o {maior} que ocupa a posição {posição_maior}')
print(f'o menor elemento digitado foi o {menor} que ocupa a posição {posição_menor}')
'''

#método do guanabara
listanum=[]
mai=men=0


for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c==0:
        mai=men=listanum[c]
    else:
        if listanum[c]>mai:
            mai=listanum[c]
        if listanum[c]<men:
            men=listanum[c]


print(f'Valores digitados: {listanum}')


print(f'maior valor é o {mai}, que ocupa a posição: ',end='')
for localização,valor in enumerate(listanum):
    if valor==mai:
        print(f'{localização}..',end='')


print()


print(f'menor valor é o {men}, que ocupa a posição: ', end='')
for localização,valor in enumerate(listanum):
    if valor==men:
        print(f'{localização}..',end='')