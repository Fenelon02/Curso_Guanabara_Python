#MODULOS

#ADCIONAR LISTAS EM OUTRA LISTA


'''
dados=['pedro',25]
pessoa=list()

#ESTE [:] CRIA UMA CÓPIA DA LISTA ANTERIOR 

pessoa.append(dados[:])
print(pessoa)
'''

'''
dados=['pedro',25]
dados_2=['Maria',19]
dados_3=['João',32]
pessoa=list()
pessoa.append(dados[:])
pessoa.append(dados_2[:])
pessoa.append(dados_3[:])
print(pessoa)'''

'''
#OUTRA FORMA DE DECLARAR A INFORMAÇÃO ACIMA

pessoa=[['Pedro', 25],['Maria',19],['João',32]]
print(pessoa)

'''

#MANIPULAÇÃO DE MÓDULOS

'''
pessoa=[['Pedro', 25],['Maria',19],['João',32]]
print(pessoa[0][0])

#vai printar a lista na posição [0] e o str na posição [0]
'''

'''
pessoa=[['Pedro', 25],['Maria',19],['João',32]]
print(pessoa[0])

#vai printar tudo na lista na posição [0]
'''

#PARTE PRÁTICA DA AULA
'''
teste=list()
teste.append('gustavo')
teste.append(40)
print(teste)
galera=[]
galera.append(teste)
teste[0]='Maria'
teste[1]=22
galera.append(teste)
print(galera)'''

'''#não vai ser aletrado pois não foi criada uma cópia da estrutura anterior'''

'''
teste=list()
teste.append('gustavo')
teste.append(40)
galera=[]
galera.append(teste[:])

#desta forma não ficará uma ligação e sim uma cópia, podendo a antiga ser alterada

teste[0]='Maria'
teste[1]=22
galera.append(teste[:])

#desta forma não ficará uma ligação e sim uma cópia, podendo a antiga ser alterada


print(galera)
'''

'''
galera=[['Júlia',18],['Alana',33],['joaquim',13],['Maria',45]]
print(galera[2][1])

#Só mais uma forma de declarar variável
'''
'''
galera=[['Júlia',18],['Alana',33],['joaquim',13],['Maria',45]]
for pessoa in galera:
    print(pessoa)

#vai printar cada lista individual, cada pessoa, com suas informações
'''

'''
galera=[['Júlia',18],['Alana',33],['joaquim',13],['Maria',45]]
for pessoa in galera:
    print(pessoa[0])

#Vai printar apenas os nomes das pessoas, pois estão na posição [0]
'''

'''
galera=[['Júlia',18],['Alana',33],['joaquim',13],['Maria',45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

#Printa a pessoa e a idade individualmente
'''

'''
pessoas=[]
dados=[]

for contador in range(0,3):
    dados.append(input('Digite seu nome: '))
    dados.append(int(input('Digite sua idade: ')))
    pessoas.append(dados[:])

#a falta do [:] iria zerar as listas, pois não geraria uma cópia da mesma
    
    dados.clear()

print(pessoas)

#vai adcionar as pessoas e seus dados na lista
'''

'''
pessoas=[]
dados=[]
total_maiores_de_idade=0
total_menores_de_idade=0

for contador in range(0,3):
    dados.append(input('Digite seu nome: '))
    dados.append(int(input('Digite sua idade: ')))
    pessoas.append(dados[:])
    dados.clear()

for populacao in pessoas:
    if populacao[1]>=21:
        total_maiores_de_idade+=1
        print(f'{populacao[0]} é maior de idade')
    else:
        total_menores_de_idade+=1
        print(f'{populacao[0]} é menor de idade')

#Vai contar cada pessoa e seus dados, neste caso, sua idade, colocada na posição [1]
#e vai armazenalos em uma váriavel printando seus nomes, em menores e maiores de idade
#e armazenar a quantidade de pessoas maiores e menores de idade

print(f'Temos {total_maiores_de_idade} maiores de idade\nE temos {total_menores_de_idade} menores de idade')

'''










































