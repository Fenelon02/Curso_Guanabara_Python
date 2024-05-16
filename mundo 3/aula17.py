# LISTAS []
'''
-LISTAS PODEM SER MODIFICADAS

Usabilidades:

-Para adcionar ítens:

    x.append('elemento')
    . adciona em ultimo

    x.insert(0,'elemento')
    . adciona na posição desejada

-Para apagar ítens:
    
    del x[posição x]
    . apaga o elemento na posição desejada

    x.pop(posição)
    . geralmente usado para apagar o último elemento, porém pode ser usado em todos os casos

    x.remove('ítem')
    . remove o ítem desejado
    . O primeiro no caso

-Para criar uma lista 

    valores=--LIST---(range(4,11))

    .o list cria ou transforma algo em lista

-Ordenar uma lista

    valores=[1,,3,10,9,16,192]

    ->x.sort()
    . vai ordenar em ordem crescente

    ->x.sort(reverse=True)
    . vai ordenar em ordem decrescente

-Ver o tamanho da lista

    len.(x)
    . Mostra o tamanho da lista


'''

# PARTE PRÁTICA

lista=[2,5,9,1]
'''
x=lista.pop()
print(x)
-mostra o ultimo removido

lista.pop()
print(lista)
-mostra como ficou a lista dps de seu ultimo ítem ser removido

for v in lista:
    print(f'{v}...')

-mostra os ítens de uma forma mais bonita

for c,v in enumerate(lista):
    print(f'na posição {c} temos o valor {v}')

-Mostra o ítem e a posição, por causa do enumerate


valores=[]
valores.append(1)
valores.append(12)
valores.append(13)
valores.append(14)

for contador in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'na posição {c} encontrei {v}.')

-Mostra o ítem e sua posição
    
valores=[]

for contador in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for posição,numero in enumerate(valores):
    print(f'na posição {posição} encontrei {numero}.')

-Mostra o ítem e sua posição, mas podendo inputar o elemento

a=[1,2,3,4,5]
b=a
b[2]=9

print(a)
print(b)

-Se alterar em um, altera nos dois, pois cria uma ligação de equidade

a=[1,2,3,4,5]
b=a[:]
b[2]=9

print(a)
print(b)

-Cria apenas uma cópia, sem ligação entre elas, por causa do --[:]--
'''

































































