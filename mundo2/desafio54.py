from datetime import date

maior=0
menor=0

for c in range(0,7):

    ano=date.today().year

    ano_de_nascimento=int(input('Digite seu ano de nascimento: '))

    idade=ano-ano_de_nascimento

    if idade>=18:
        maior+=1
    else:
        menor+=1


print(f'tivemos {maior} pessoas maiores de idade')
print(f'Tivemos {menor} pessoas menores de idade')


