'''
Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
'''

dados_do_aluno=dict()

dados_do_aluno['nome']=input('Digite seu nome: ')
dados_do_aluno['media']=float(input('Digite sua média: '))

if dados_do_aluno['media']>=7:
    dados_do_aluno['situacao']='Aprovado.'

elif 5<=dados_do_aluno['media']<7 :
    dados_do_aluno['situacao']='Recuperação.'

else:
    dados_do_aluno['situacao']='Reprovado.'

print()
for key,value in dados_do_aluno.items():
    print(f'{key} é correspondente a {value}')