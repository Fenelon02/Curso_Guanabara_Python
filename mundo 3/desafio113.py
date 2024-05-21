'''Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

# MEU CÓDIGO
'''ESQUECI DE POR O KeyboardInterrupt''' 
'''
def leitor_de_numeros_inteiros(elemento=''):

    elemento=input('Digite um número inteiro: ').strip()

    try:
        int(elemento)
        return elemento
    
    except:
        
       while True:

            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO\033[m')
            elemento=input('Digite um número inteiro: ').strip()

            try:
                elemento=int(elemento)
                return elemento

            except:
                continue



def leitor_de_numeros_reais(elemento=''):

    elemento=input('Digite um número real: ').strip()

    try:
        float(elemento)
        return elemento
    
    except:

        while True:

            print('\033[0;31mERRO! DIGITE UM NÚMERO REAL\033[m')
            elemento=input('Digite um número real: ').strip()

            try:
                elemento=float(elemento)
                return elemento

            except:
                continue


inteiro=(leitor_de_numeros_inteiros())
real=(leitor_de_numeros_reais())

print(f'O valor inteiro digitado foi {inteiro} e o valor real digitado foi {real}')
'''
#CÓDIGO GUANABARA

def leitor_de_numeros_inteiros(elemento=''):
    while True:

        try:
            elemento=int(input(elemento))
            return elemento
        
        except KeyboardInterrupt:
                print('Usuário optou por não digitar este valor')
                return 0
        
        except:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO\033[m')
            continue



def leitor_de_numeros_reais(elemento=''):
    while True:

        try:
            elemento=float(input(elemento))
            return elemento
        
        except KeyboardInterrupt:
                print('Usuário optou por não digitar este valor')
                return 0
        
        except:
            print('\033[0;31mERRO! DIGITE UM NÚMERO REAL\033[m')
            continue


# inteiro=leitor_de_numeros_inteiros('Digite um número inteiro: ')
# real=leitor_de_numeros_reais('Digite um número real: ')

# print(f'O valor inteiro digitado foi {inteiro} e o valor real digitado foi {real}')
