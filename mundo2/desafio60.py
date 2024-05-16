from math import factorial

print('\nPrograma desenvolvido para obter fatorial do número desejado.')

parar=int(input('\nDigite\n[1]parra começar\n[2]para parar\n'))



while parar!=3:
    
    numero=int(input('Digite um número e otenha seu fatorial: '))

    fatorial=factorial(numero)

    print(f'O fatorial de {numero} é {fatorial}.')

    parar=int(input('Digite\n[1]para continuar\n[2]para trocar o número\n[3]para parar\n'))



    if parar==2:

        numero_novo=int(input('Digite o número que deseja: '))

        fatorial_novo=factorial(numero_novo)

        print(f'O fatorial de {numero_novo} é {fatorial_novo}.')

        parar=int(input('Digite\n[1]para continuar\n[2]para trocar o número\n[3]para parar\n'))

    