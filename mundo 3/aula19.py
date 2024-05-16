#DICIONÁRIOS EM PYTHON

'''
-Idenrificados por {}
'''
'''
#Para criar um dicionário
dados=dict()
ou
dados={'nome':'Pedro','idade':25}
print(dados['nome'])

#append não funciona, ao inves disso, se cria outra variável,como escrito abaixo
dados['sexo']='M'
print(dados['sexo'])

#para eliminar um elemento
del dados['idade']
print(dados)


#para printar apenas o conteúdo
filme={'titulo':'star wars',
 'ano':1997,
 'diretor':'george lucas' 
}

print(filme.values())

#para printar o nome do conteúdo, ex: título
filme={'titulo':'star wars',
 'ano':1997,
 'diretor':'george lucas' 
}
print(filme.keys())

#para printar tudo
filme={'titulo':'star wars',
 'ano':1997,
 'diretor':'george lucas' 
}
print(filme.items())

#para printar título do conteúdo e o conteúdo
filme={'titulo':'star wars',
 'ano':1997,
 'diretor':'george lucas' 
}
for key,value in filme.items():
    #para cada nome do conteúdo e valores(conteúdo) contido em todo dicionário 'filmes'.
    print(f'o {key} é {value}')
'''

#PARTE PRÁICA

'''
pesssoas={'nome':'gustavo','sexo':'M','idade':38}
#como está sob aspas simples, para printar uso aspas duplas
#na hora de referenciar se usa colchetes, para declarar se usa chaves.
print(f'o {pesssoas["nome"]} tem {pesssoas["idade"]} anos.')

pesssoas={'nome':'gustavo','sexo':'M','idade':38}
for keys in pesssoas.keys():
    print(keys)
    #vai mostrar as cada uma das chaves,títulos.

pesssoas={'nome':'gustavo','sexo':'M','idade':38}
for keys,values in pesssoas.items():
    #itens é tudo no dicionário
    print(f'{keys}={values}')
    #vai mostrar as cada uma das chaves e seus respectivos valores.

pesssoas={'nome':'gustavo','sexo':'M','idade':38}
for keys in pesssoas.values():
    print(keys)
    #vai printar cada cois,cada ítem do dicionário

pesssoas={'nome':'gustavo','sexo':'M','idade':38}

del pesssoas['sexo']

#vai apagar o sexo da lista

for keys,values in pesssoas.items():
    print(f'{keys}={values}')


    
pesssoas={'nome':'gustavo','sexo':'M','idade':38}

pesssoas['nome']='Leandro'

#vai substituir gustavo por Leandro

for keys,values in pesssoas.items():
    print(f'{keys}={values}')  

    

pesssoas={'nome':'gustavo','sexo':'M','idade':38}

pesssoas['peso']=98.5

#vai adcionar o 'peso' no dicionário

for keys,values in pesssoas.items():
    print(f'{keys}={values}')  

    

brasil=[]

estado_1={'uf':'Rio de Janeiro','sigla':'RJ'}
estado_2={'uf':'São Paulo','sigla':'SP'}

brasil.append(estado_1)
brasil.append(estado_2)

print(brasil[0]['uf'])

#vai printar o dicionário ['uf'] que está na posição [0] da lista.
'''



estado=dict()
brasil=list()
for contador in range(0,3):
    estado['Unidade federativa'] = str(input('Digite o Estado: '))
    estado['sigla']  = str(input('Digite sua sigla: '))
    brasil.append(estado.copy())
    #cria uma cópia do dicionário, podendo adcionar mais ítens na lista 'brasil' sem se repetirem

for state in brasil:
    for key,value in state.items():
        print(f'O campo {key} tem valor {value}.')






























