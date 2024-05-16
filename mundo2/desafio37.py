print('Digite um número, e tecle \n1 paraa converte-lo para binário \n2 para octal \ne 3 para hexadecimal')

numero=int(input('Digite o número escolhido: '))
escolha=int(input('Digite o número que representa a conversão escolhida: '))

if escolha==1:
    binário=bin(numero)
    print(binário)
elif escolha==2:
    octal=oct(numero)
    print(octal)
else:
    hexadecimal=hex(numero)
    print(hexadecimal)