'''
Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto:
NEGADO
OPCIONAL 
e OBRIGATÓRIO nas eleições.
'''
import time

def voto(ano_de_nascimento):

    tempo_atual=time.localtime()
    ano_atual=tempo_atual.tm_year
    
    idade=ano_atual-ano_de_nascimento
    
    if idade>=18 and idade<66:
        return f'Com {idade} de idade: Voto obrigatório'
    
    elif 16<=idade<18 or idade>65:
        return f'Com {idade} de idade: Voto opcional'
    
    else:
        return f'Com {idade} de idade:  Voto negado'

ano_de_nascimento=int(input('Digite seu ano de nascimento: '))
print(voto(ano_de_nascimento))
