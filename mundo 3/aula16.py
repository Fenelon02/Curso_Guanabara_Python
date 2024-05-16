'''                         TUPLAS

lanche=[]

#TUPLAS SÃO <<IMUTÁVEIS>> 
#PODE MISTURAR STR,INT,FLOAT,ETC



while True:
    lanche=('hamburguer','suco','pizza','pudim')

    print(lanche[-1])
    #vai printar o ultimo elemento

    

lanche=('hamburguer','suco','pizza','pudim')
for c in lanche:
    print(c)

    #printa cada um dos elementos




lanche = 'hamburguer','suco','pizza','pudim'

#tupla pode ser sem parênteses

print(lanche[-2])

#vai printar o eleemento na posição 1



lanche = 'hamburguer','suco','pizza','pudim'

#tupla pode ser sem parênteses

print(lanche[:2])

#vai printar os elementos da posiçaõ 0, o primeiro até a posição 1



lanche = 'hamburguer','suco','pizza','pudim'

#tupla pode ser sem parênteses

print(lanche[-2:])

#vai printar os elementos da posiçaõ -2,
no caso, o antepenultimo, até o fim.



lanche=('hamburguer','suco','pizza','pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')

#só pra bestar



lanche=('hamburguer','suco','pizza','pudim')

for contador in range(0,len(lanche)):
    print(lanche[contador])

#outra forma de fazer o problema acima



lanche=('hamburguer','suco','pizza','pudim')

for contador in range(0,len(lanche)):
    print(f'este lanche {lanche[contador]} está na posição {contador}')

#mostra a posição do ítem



lanche=('hamburguer','suco','pizza','pudim')

for posiçao, contador in enumerate(lanche):
    print(f'este lanche:\n{contador} está na posição {posiçao}')

#mostra a posição do ítem de outra forma



lanche=('hamburguer','suco','pizza','pudim')

print(sorted(lanche))

#mostra a lista em ordem alfabética, numérica, etc



a=(1,2,3,4)
b=(0,9,8,7,6,5,4)

c=a+b

print(c)

#vai unir as tuplas



a=(1,2,3,4)
b=(0,9,8,7,6,5,4)

c=a+b

print(c.count(4))

#conta quantas vezes um certo elemento aparece



a=(1,2,3,4)
b=(0,9,8,7,6,5,4)

c=a+b

print(c.index(8))

#mostra em que posição certo elemento está, e/ou aparece primeiro

print(c.index(2,1))

#mostra em que posição certo elemento está, começando da posição 1



pessoa=('eu', 16,'sla')
del(pessoa)

#vai apagar a variável pessoa

'''
