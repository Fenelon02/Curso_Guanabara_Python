import random

contador=0
while True:
    escolha_jogador=str(input('Você deseja ser par ou ímpar? [I/P]: ')).lower().strip()

    numero_jogador=int(input('Digite um número: '))

    numeros_computador=[1,2,3,4,5,6,7,8,9,10]

    x=random.choice(numeros_computador)

    vencedor=x+numero_jogador
    
    if escolha_jogador=='i' and vencedor%2!=0:
        print(f'Total foi {vencedor}')
        print(f'Computador escolheu par, e jogou o número {x}')
        print(f'Jogador escolheu ímpar, e jogou o número {numero_jogador}')
        contador+=1
        print(f'Jogador venceu {contador} vezes!')
        parar=int(input('Deseja parar?\n[1]-sim\n[2]-não\n'))
        if parar==1:
            print('Tchau')
            break
        

    if escolha_jogador=='p' and vencedor%2==0:
        print(f'Total foi {vencedor}')
        print(f'Computador escolheu ímpar, e jogou o número {x}')
        print(f'Jogador escolheu par, e jogou o número {numero_jogador}')
        contador+=1
        print(f'Jogador venceu {contador} vezes!')
        parar=int(input('Deseja parar?\n[1]-sim\n[2]-não\n'))
        if parar==1:
            print('Tchau')
            break

    if escolha_jogador=='i' and vencedor%2==0:
        print(f'Total foi {vencedor}')
        print(f'Computador escolheu par, e jogou o número {x}')
        print(f'Jogador escolheu ímpar, e jogou o número {numero_jogador}')
        print('Computador venceu!')
        parar=int(input('Deseja parar?\n[1]-sim\n[2]-não\n'))
        if parar==1:
            print('Tchau')
            break

    if escolha_jogador=='p' and vencedor%2!=0:
        print(f'Total foi {vencedor}')
        print(f'Computador escolheu par, e jogou o número {x}')
        print(f'Jogador escolheu ímpar, e jogou o número {numero_jogador}')
        print('Computador venceu!')
        parar=int(input('Deseja parar?\n[1]-sim\n[2]-não\n'))
        if parar==1:
            print('Tchau')
            break
    