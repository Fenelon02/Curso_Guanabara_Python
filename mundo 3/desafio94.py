'''
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''

informacoes_pessoais=dict()
bando_de_dados_das_pessoas=[]
lista_mulheres=[]
prosseguir='s'
total_pessoas=0
media_de_idade=0
media_de_idade_pessoal=0
pessoas_mais_velhas=[]

while prosseguir in 'Ss':

    informacoes_pessoais['nome']=input('Digite seu nome: ')
    informacoes_pessoais['sexo']=input('Digite seu sexo: [M/F]').lower().strip()[0]

    while informacoes_pessoais['sexo'] not in 'MmFf':
        informacoes_pessoais['sexo']=input('ERRO! Digite seu sexo: [M/F]').lower().strip()[0]

    informacoes_pessoais['idade']=int(input('Digite sua idade: '))
    
    prosseguir=input('Deseja prosseguir? ')
    while prosseguir not in 'SsNn':
        prosseguir=input('ERRO! Deseja prosseguir? ')
    

    total_pessoas+=1

    media_de_idade_pessoal+=informacoes_pessoais['idade']
    media_de_idade=media_de_idade_pessoal/total_pessoas

    if informacoes_pessoais['sexo']=='f':
        lista_mulheres.append(informacoes_pessoais['nome'])

    bando_de_dados_das_pessoas.append(informacoes_pessoais.copy())

'''for pessoa in bando_de_dados_das_pessoas:
    if pessoa['idade']>media_de_idade:
        pessoas_mais_velhas.append(pessoa)
'''
print(f'Foram cadastradas {total_pessoas}')
print(f'A média de idade destas pessoas é de {media_de_idade:.0f} anos.')
print(f'mulheres cadastradas:')
for mulheres in lista_mulheres:
    print(f'{mulheres}')
print('Pessoas acima da média de idade: ')
'''for pessoa in pessoas_mais_velhas:
    print(f'{pessoa['nome']}, sexo={pessoa['sexo']}, idade={pessoa['idade']}')'''
for pessoa in bando_de_dados_das_pessoas:
    if pessoa['idade']>media_de_idade:
        for key,value in pessoa.items():
            print(f'{key} = {value},',end=' ')

