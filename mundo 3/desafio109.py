'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
---desenvolvida no desafio 108.---
'''

import modulo_desafio_109
numero=float(input('Digite um número: '))

#o FALSE serve para mostrar ou não o número formatado.

print(f'o valor {modulo_desafio_109.valor_formatado(numero)} aumentando 10% temos {modulo_desafio_109.aumentar(numero,10)}')
print(f'o valor {modulo_desafio_109.valor_formatado(numero)} diminuindo 10% temos {modulo_desafio_109.diminuir(numero,10)}')
print(f'O dobro de {modulo_desafio_109.valor_formatado(numero)} é igual a {modulo_desafio_109.dobro(numero)}')
print(f'A metade de {modulo_desafio_109.valor_formatado(numero)} é igual a {modulo_desafio_109.metade(numero,)}')