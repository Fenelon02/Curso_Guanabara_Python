'''
crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt('Digite um n: ')
'''

def leitor_de_numeros_inteiros(elemento):

    elemento=input('Digite um número: ')

    if elemento.isnumeric():
        elemento=int(elemento)
        return elemento
    
    else:
        while elemento is not elemento.isnumeric:

            # este \033[0;31 começa a cor vermelha e este \033[m termina
            
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO\033[m')
            elemento=input('Digite um número: ')
            if elemento.isnumeric():
                elemento=int(elemento)
                return elemento


numero=leitor_de_numeros_inteiros('Digite um número: ')
print(f'Você digitou o número {numero}')