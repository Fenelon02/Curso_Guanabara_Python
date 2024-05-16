import random

prossegue=input('Digite se quer jogar. [sim/nao] ').lower().strip()[0]

lista=[1,2,3,4,5,6,7,8,9,10]

computador_escolhe_número= lista

x=random.choice(lista)

contagem=1

while prossegue=='s':
    numero_jogador=int(input('Digite um número: '))

    
    if numero_jogador==x:
        print('Parabéns, o número é igual')

        print(f'Você jogou {contagem} vez(es) para ganhar')
        break

    else:
        contagem+=1

        if numero_jogador>x:
            print('Número maior, digite um valor menor.')
        else:
            print('Número menor, digite um valor maior.')