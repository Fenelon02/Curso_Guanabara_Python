media=0

total=0

maior=0

nome_velho=''


for c in range(1,5):
    sexo=input('Digite:\n[m] para homem\n[F] para mulher\n')
    idade=int(input('Digite sua idade: '))
    nome=input('Digite seu nome: ')


    media+=idade
    total=media/4

    if sexo in 'Mn' and c==1:
        maior=idade
        nome_velho=nome

    if sexo in 'Mn' and idade>maior:
        maior = idade
        nome_velho=nome 

   

print(f'{total}')
print(maior,nome_velho)


    
    
    