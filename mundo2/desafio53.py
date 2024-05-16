vezes=int(input('Digite a quantidade de vezes que deseja rodar o programa: '))

for i in range(1,vezes+1):

    palavra_1=input('Digite uma palavra e veja se ela é um palíndromo: ')

    palavra_1= palavra_1.replace(" ", "").lower()

    
    if palavra_1==palavra_1[::-1]:
        print(f'{palavra_1} É um palíndromo!')
    else:
        print(f'{palavra_1} Não é um palíndromo.')
