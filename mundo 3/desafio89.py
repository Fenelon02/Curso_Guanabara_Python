'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.
'''

lista_total=[]

aluno=input('Digite o nome do aluno: ')
nota_1=float(input('Digite a 1 nota do aluno: '))
nota_2=float(input('Digite a 2 nota do aluno: '))
media=((nota_1+nota_2)/2)
lista_total.append(list((((aluno,nota_1,nota_2,media)))))

prosseguir=input('Quer continuar? [S/N]').lower().strip()[0]

while prosseguir not in "SsNn":
    prosseguir=input('Valor não aceito. Quer continuar? [S/N]').lower().strip()[0]

while prosseguir in 'SsNn':

    if prosseguir in 'Nn':
        break
    aluno=input('Digite o nome do aluno: ')
    nota_1=float(input('Digite a 1 nota do aluno: '))
    nota_2=float(input('Digite a 2 nota do aluno: '))
    media=(nota_1+nota_2)/(2)
    lista_total.append(list((((aluno,nota_1,nota_2,media)))))

    prosseguir=input('Quer continuar? [S/N]').lower().strip()[0]
print(f'{'N':<4}{'Nome':<10}{'média':>8}')
for indice,valor in enumerate(lista_total):
    print(F'{indice+1:<4}{valor[0]:<10}{valor[3]:>8}')

mostrar_notas=int(input('Deseja mostrar as notas de qual aluno? [999] PARA '))
while mostrar_notas!=999:
    print(f'notas de {lista_total[mostrar_notas-1][0]} são [{lista_total[mostrar_notas-1][1]}] [{lista_total[mostrar_notas-1][2]}]')
    mostrar_notas=int(input('Deseja mostrar as notas de qual aluno? [999] PARA '))
print('Programa finalizado, volte sempre.')