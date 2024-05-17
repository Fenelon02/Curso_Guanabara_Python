'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
import time

#para extrair o ano atual
tempo_atual=time.localtime()
ano_atual=tempo_atual.tm_year

dados_pessoais={}
dados_pessoais['nome']=input('Digite seu nome: ')
dados_pessoais['idade']=(ano_atual-(int(input('Digite seu ano de nascimento: '))))
dados_pessoais['carteira de trabalho']=int(input('Digite seu CTPS\n[0]para inexistente '))


if dados_pessoais['carteira de trabalho']!=0:
    dados_pessoais['ano de contratacao']=int(input('Digite seu ano de contratação: '))
    dados_pessoais['salario']=float(input('Digite seu salário: '))
    dados_pessoais['idade de aposentadoria']=dados_pessoais['idade']+((dados_pessoais['ano de contratacao']+35)-ano_atual)
    print()
    for key,value in dados_pessoais.items():
        print(f'{key} tem valor {value}')
else:
    print()
    for key,value in dados_pessoais.items():
        print(f'{key} tem valor {value}')

    
    