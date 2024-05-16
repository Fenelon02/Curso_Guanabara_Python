from random import randint

#o tuple vai converter a lista para uma tupla
#tupla_numeros = tuple(random.randint(1, 100) for _ in range(5))

numeros_sorteados=(randint(0,10), randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),
randint(0,10),randint(0,10),randint(0,10),randint(0,10))

LISTA_FINAL=(sorted(numeros_sorteados))

print(f'Estes foram os números sorteados: {numeros_sorteados}')

#print(f'Este é o menor valor: {LISTA_FINAL[0]}')

print(f'Este é o menor valor: {min(LISTA_FINAL)}')

#print(f'Este é o maior valor: {LISTA_FINAL[-1]}')

print(f'Este é o maior valor: {max(LISTA_FINAL)}')
